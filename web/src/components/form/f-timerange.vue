<!--
 * @Filename     : scroll_step.vue 
 * @Description  : wjt-前端-逐步滚动  line_count->行数 duration->滚动时间
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


// 定义响应式数据
const scrolling = ref(true);
const line = ref(1);
const scroll_duration = ref('0');
const scroll_top = ref('0');
const scroll_body = ref(null);
let animationFrameId = null;
const duration = props.duration ? parseInt(props.duration) : 2000;

// 定义滚动逻辑
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

            // 使用 setTimeout 以实现更平滑的动画
            animationFrameId = setTimeout(() => {
                requestAnimationFrame(scrollStep);
            }, duration);
        }
    }
};

const start = () => {
    if (!animationFrameId) {
        scrollStep(); // 开始滚动
    }
};

// 暂停滚动
const pauseScroll = () => {
    scrolling.value = false;
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        clearTimeout(animationFrameId);
        animationFrameId = null;
    }
};

// 恢复滚动
const resumeScroll = () => {
    scrolling.value = true;
    start(); // 恢复滚动
};

onMounted(() => {
    start();
});

onBeforeUnmount(() => {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        clearTimeout(animationFrameId);
    }
});

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
