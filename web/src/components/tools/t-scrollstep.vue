<!--
 * @Filename     : scroll_step.vue
 * @Description  : wjt-前端-逐步滚动  line_count->行数
 * @Author       : xingshuyin xingshuyin@outlook.com
 * @Date         : 2022-10-24 09:53:23
 * @LastEditors  : xingshuyin xingshuyin@outlook.com
 * @LastEditTime : 2022-11-17 14:32:07
 * Copyright (c) 2022 by Research Center of Big Data and Social Computing DARG, All Rights Reserved.
-->
<script setup>
// 注意:  父组件必须有宽高
import { ref, onMounted, onUpdated, onBeforeUnmount } from 'vue';
const props = defineProps(['line_count', 'duration']); // defineProps的参数, 可以直接使用
const scroll_item_a = ref(null)
const scroll = ref(null)
const scroll_body = ref(null)
var scroll_height = ref(0)
var scroll_top = ref('')
var scroll_duration = ref('1000ms')
var scrolling = ref(true)
const step = ref(null)
const line = ref(0)
// const start = () => {
//     step.value = setInterval(() => {
//         if (scrolling.value) {
//             if (line.value == props.line_count + 1) {
//                 setTimeout(() => {
//                     line.value = 1
//                     scroll_duration.value = '0'
//                     scroll_top.value = '-5px'
//                     console.log('reset scroll_top', scroll_top.value);
//                 }, 0)
//             }
//             scroll_height.value = scroll_body.value.offsetHeight / 2 / props.line_count  //获取滚动目标的高度
//             scroll_duration.value = '1000ms'
//             scroll_top.value = '-' + scroll_height.value * line.value + 'px'
//             console.log('scroll_top', scroll_top.value);
//             line.value += 1
//         }

//     }, 1000)
// }
let animationFrameId = null;
const duration = props.duration ? parseInt(props.duration) : 2000
const start = () => {
    const scrollStep = () => {
        if (scrolling.value) {
            if (line.value == props.line_count + 1) {
                line.value = 1;
                scroll_duration.value = '0';
                scroll_top.value = '-5px';
                console.log('重置 scroll_top', scroll_top.value);

                // 立即触发下一步滚动
                animationFrameId = requestAnimationFrame(scrollStep);
            } else {
                const scrollHeight = scroll_body.value.offsetHeight / (2 * props.line_count);
                scroll_duration.value = `${duration}ms`;
                scroll_top.value = `-${scrollHeight * line.value}px`;
                console.log('scroll_top', scroll_top.value);
                line.value += 1;

                // 使用 requestAnimationFrame 以实现更平滑的动画
                animationFrameId = requestAnimationFrame(() => {
                    setTimeout(scrollStep, duration);
                });
            }
        }
    };

    scrollStep(); // 开始滚动
};
// 暂停滚动
const pauseScroll = () => {
    scrolling.value = false;
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
};

// 恢复滚动
const resumeScroll = () => {
    scrolling.value = true;
    // startTime = null; // 重置开始时间
    start(); // 恢复滚动
};
onMounted(() => {
    start()
})
onBeforeUnmount(() => {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }
})
// TODO:动画-无限滚动
</script>
<template>
    <div class="scroll" ref="scroll" :style="{ height: '100%' }" @mouseenter="pauseScroll" @mouseleave="resumeScroll">
        <div class="scroll-body" ref="scroll_body">
            <slot></slot>
            <slot></slot>
        </div>

    </div>
</template>
<style scoped lang="scss">
.scroll {
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.scroll-body {
    // height: fi;
    transition-duration: v-bind(scroll_duration);
    top: v-bind(scroll_top);
    position: relative;
    width: 100%;
}
</style>
