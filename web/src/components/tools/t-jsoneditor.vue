<template>
    <div ref="editor" id="jsoneditor">

    </div>
</template>
<script setup>
import JSONEditor from 'jsoneditor'
import 'jsoneditor/dist/jsoneditor.css'
import { onBeforeUnmount, onMounted, watch } from 'vue';
const props = defineProps({
    modelValue: {
        type: Object, default: () => ({
            'name': '黑龙江省文化和旅游厅-直属动态',  // 规则名称
            'start_urls': 'https://wlt.hlj.gov.cn/wlt/c114162/common_list.shtml',  // 开始页(逗号分隔)
            'allowed_domains': 'hebust.edu.cn',

            // 自定义分页链接
            'page_format': 'https://wlt.hlj.gov.cn/common/search/page={}',  // {}会被替换为页数, 页数是和下面的三条有关
            'page_format_shift': "str(num)",  // "'_'+str(num) if num > 1 else ''"  num为根据page_min和page_max遍历出的的变量, 因为页数可能是不完全规则的
            'page_min': 1,  // 最小页数
            'page_max': 1,  // 最大页数

            'json_page': true,  // 是否JSON的分页
            'json_item': false,  // 是否JSON的item
            'json_item_format': 'https://wlt.hlj.gov.cn{}',  // JSON分页时, item链接的format, { num }
            'json_item_format_shift': '',  // item标识的转换 变量为num, 有时候获取的标识并不能直接放到链接中, 就需要转换一下

            // xpath获取分页
            'get_page': null,  // 分页链接提取区域xpath(和自定义分页链接选其一)

            // xpath获取文章链接
            'get_item': '$..url',  // 内容链接提取区域xpath或文章标识的jsonpath

            // 有了get_img就是纯图片抓取 contentrule无效
            'get_img': null,

            // 获取各种数据
            'contentrule': {
                // 'img': { 'path': '//div[@class="single-content"]//img/@src', 're': '' }, //
                '标题': { 'path': '//title//text()', 're': "" },  // path可以是html的xpath也可以是jsonpath(json_item为True的话)
                '时间': { 'path': '//div[@class="date"]//text()', 're': "日期：(.*).*?" },
                '内容': { 'path': '//div[@id="detailContent"]//text()', 're': "" },
                '来源': { 'path': '//span[@class="ly"]//text()', 're': "来源：(.*).*?" },
            },
            // 分页 / 文章链接过滤
            're_page': null,  // 分页链接正则, 不填就是.*
            're_item': null,  // 文章链接正则, 不填就是.*
        })
    }, //父传子数据
}); //子向父传数据
const attrs = reactive({editor:null});

const emits = defineEmits(['update:modelValue']); //父调用子函数
// emits('update:modelValue', props.modelValue); //子调用父函数
const editor = ref(null)
onMounted(() => {
    const container = document.getElementById('jsoneditor');
    attrs.editor = new JSONEditor(container, {
        modes: ['code', 'tree', 'form'],
        onChange: function () {

            emits('update:modelValue', attrs.editor.get());
        }
    })
    attrs.editor.set(props.modelValue)
})
onBeforeUnmount(() => {
    attrs.editor.destroy()
})
</script>
<style scoped lang='scss'>
#jsoneditor {
    min-width: 500px;
    // min-height: 500px;
    font-family: '宋体';
}
</style>
