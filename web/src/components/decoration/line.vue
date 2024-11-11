<template>
    <div class="shape-container" ref="ShapeContainer">
        <!-- U形SVG动画 -->
        <svg class="u-shape" viewBox="0 0 290 55" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">;
            <polyline points="145,35 80,35 74,26 59,26 53,18 0,18" stroke="url(#gradient)" fill="none"
                :style="{ animation: 'dash 2s linear infinite' }" stroke-width="4" />
            <polyline points="145,35 210,35 216,26 231,26 237,18 290,18" stroke="url(#gradient)" fill="none"
                :style="{ animation: 'dash 2s linear infinite' }" stroke-width="4" />

            <!-- <polyline points="145,43 210,43 211,43" stroke="white" fill="none" stroke-width="4"
                :style="{ animation: 'dash 2s linear infinite' }" />
            <polyline points="145,43 80,43 79,43" stroke="white" fill="none" stroke-width="4"
                :style="{ animation: 'dash 2s linear infinite' }" /> -->

            <line x1="145" y1="42" x2="210" y2="42" stroke-width="4" stroke="white"
                :style="{ animation: 'dash 2s linear infinite' }" />
            <line x1="145" y1="42" x2="80" y2="42" stroke-width="4" stroke="white"
                :style="{ animation: 'dash 2s linear infinite' }" />

            <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#00f6ff;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#0066ff;stop-opacity:1" />
                </linearGradient>
                <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color: #ff0000; stop-opacity: 1" /> <!-- 红色 -->
                    <stop offset="100%" style="stop-color: #0000ff; stop-opacity: 1" /> <!-- 蓝色 -->
                </linearGradient>
            </defs>
        </svg>

        <!-- 标题文本 -->
        <!-- <div class="title">
            <slot></slot>
        </div> -->
    </div>
</template>

<script setup>

</script>

<style scoped>
.shape-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}


.title {
    position: relative;
    font-size: 35px;
    /* color: #0066ff; */
    font-weight: bold;
    /* background-color: white; */
    padding: 2px 10px;
    white-space: nowrap;
    /* width: 50%; */
}


</style>