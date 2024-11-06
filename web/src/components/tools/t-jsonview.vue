<template>
    <div ref="editor" id="jsonview">

    </div>
</template>
<script setup>
import JSONEditor from 'jsoneditor'
import 'jsoneditor/dist/jsoneditor.css'
import { onBeforeUnmount, onMounted, watch } from 'vue';
const props = defineProps({
    data: {
        type: Object, default: () => ({})
    }, //父传子数据
}); //子向父传数据
const editor = ref(null)
onMounted(() => {
    const container = document.getElementById('jsonview');
    const options = {
        // 这里可以设置你需要的选项
        mode: 'view',
        mainMenuBar: false,
        navigationBar: false,
        statusBar: false,
    }
    editor.value = new JSONEditor(container, options)
    editor.value.set(props.data)
})
onBeforeUnmount(() => {
    editor.value.destroy()
})
</script>
<style scoped lang='scss'>
#jsonview {
    min-width: 500px;
    // min-height: 500px;
    font-family: '宋体';
}
</style>
