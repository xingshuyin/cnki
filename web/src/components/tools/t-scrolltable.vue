<!--
 * @Filename     : scroll_table.vue
 * @Description  : wjt-前端-平滑滚动列表
 * @Author       : xingshuyin xingshuyin@outlook.com
 * @Date         : 2022-11-08 10:02:56
 * @LastEditors  : xingshuyin xingshuyin@outlook.com
 * @LastEditTime : 2022-11-17 14:33:14
 * Copyright (c) 2022 by Research Center of Big Data and Social Computing DARG, All Rights Reserved.
-->
<script setup>
//import { ref } from 'vue';
//import {useRoute, useRouter} from 'vue-router';
//const route = useRoute() //当前路由

import { reactive } from 'vue';
// import scroll from "./scroll.vue"
const router = useRouter() //全局路由对象
const props = defineProps(['data', "columus", "media_type"]); // defineProps的参数, 可以直接使用
//const emits = defineEmits(['onclick']); // emits 触发父组件函数
//const map = ref(null); //获取ref值为map的元素
//defineExpose({ map,}); //暴露组件的内容, 父组件通过组件对象(如ref)的value获取暴露的对象

console.log(props.columus, props.data)

const columnss = reactive([
    {
        key: "name",
        label: "名称",
        flex: "1",

    },
    {
        key: "date",
        label: "时间",
        flex: "1",

    },
])
const tableData = [
    {
        date: '2016-05-03',
        name: 'Tom',
    },
]
console.log(props)
</script>
<template>
    <div class="scroll-table">
        <div class="scroll-table-head">
            <div class="scroll-table-cell" v-for="j in columus" :style="{ flex: j?.flex ?? '', textAlign: j?.align ?? 'center' ,width: j?.width ?? 'auto'}">
                {{ j.label }}
            </div>
        </div>
        <div class="scroll-table-body">
            <t-scroll style="height: 100%;">
                <div>
                    <div :class="index % 2 == 0 ? 'scroll-table-body-line even' : 'scroll-table-body-line odd'"
                        v-for="i, index in data">
                        <!-- <div class="scroll-table-body-line-detail"
                            @click="router.push({ name: 'single', query: { id: i.id, media_type: media_type } })">
                            <el-button icon="Search" circle class="w10px h10px" />
                        </div> -->
                        <div class="scroll-table-cell" v-for="j in columus" :style="{ flex: j?.flex ?? '', textAlign: j?.align ?? 'left' ,width: j?.width ?? 'auto'}">
                            <span v-if="j?.key == 'index'">
                                {{ index + 1 }}
                            </span>
                            <div class="roll" v-if="j?.roll">
                                <a :href="j.url(i)" v-if="j?.url" style="color: white;" target="_blank">{{ j?.shift ? j.shift(i[j.key]) : i[j.key]}}</a>
                                <span v-else>{{ j?.shift ? j.shift(i[j.key]) : i[j.key]}}</span>
                            </div>
                            <span v-else>
                                {{ j?.shift ? j.shift(i[j.key]) : i[j.key]}}
                            </span>
                        </div>
                    </div>
                </div>
            </t-scroll>
        </div>
    </div>
</template>
<style scoped lang='scss'>
.scroll-table {
    --height-head: 30px;
    --cell-padding: 0 10px;

    &-head {
        width: 100%;
        height: var(--height-head);
        display: flex;
        background-color: rgba(255, 255, 255, 0.158);
        color: rgb(255, 255, 255);
        border-radius: 5px;

        .scroll-table-cell {
            overflow: hidden;
            text-align: center;
            white-space: nowrap;
            // padding: var(--cell-padding);
            font-size: 16px;
            height: var(--height-head);
            line-height: var(--height-head);
        }
    }

    &-body {
        width: 100%;
        height: calc(100% - var(--height-head));
        overflow: hidden;
        display: flex;
        flex-direction: column;
        background-color: rgba(106, 188, 255, 0.068);
        border-radius: 5px;

        &-line {
            display: flex;
            width: 100%;
            height: 25px;
            // margin-bottom: 5px; //有margin就会跳

            .scroll-table-cell {
                box-sizing: border-box;
                line-height: 25px;
                overflow: hidden;
                padding: var(--cell-padding);
                // border: 1px solid white;
                text-align: center;

                .roll {
                    width: max-content;
                }

                .roll:hover {
                    text-align: center;
                    animation: 6s linear wordroll infinite;
                }
            }

            &-detail {
                float: left;
                position: absolute;
                display: none;
            }
        }

        .even {
            background-color: rgba(255, 255, 255, 0.055);
        }

        .odd {
            background-color: rgba(0, 0, 0, 0);
        }

        &-line:hover>.scroll-table-body-line-detail {
            display: block;
        }
    }
}

@keyframes wordroll {
    from {
        /* transform: translateX(70%); */
        /* transform: translateX(0px); */
        /* webkittransform: translateX(0px); */
    }

    to {
        transform: translateX(-70%);
        /* webkittransform: translateX(120%); */
    }
}
</style>
