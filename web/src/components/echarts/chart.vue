<template>
    <div :class="{'chart-container':true, 'boxall':show_corner}">
        <div v-if="title" style="display: flex;flex-direction: column;" class="my-chart">
            <div class="title">
                {{ title }}
            </div>
            <div ref="chartRef" style="width: 100%;flex: 1;"></div>
        </div>
        <div v-else ref="chartRef" class="my-chart">
        </div>
        <div :class="{'boxfoot':show_corner}"></div>
    </div>

</template>
<script setup lang="ts">
import { defineProps, onBeforeUnmount, onMounted, ref } from "vue";
import { ResizeObserver } from '@juggle/resize-observer';   // npm i @juggle/resize-observer  //TODO:监听元素大小变化
import echarts from "../../hooks/echarts"; //TODO:echarts原始组件
const props = defineProps({
    option: {
        default: {},
    },
    title: {
        default: null
    },
    show_corner: {
        default: false
    }
});
const chartRef = ref<HTMLDivElement>();
let chart: echarts.ECharts | null = null;
const ro = new ResizeObserver((entries, observer) => {
    chart?.resize()
});
ro.observe(document.body);
onMounted(() => {
    setTimeout(() => {
        initChart();
    }, 20);
});

const initChart = () => {
    chart = echarts.init(chartRef.value as HTMLDivElement);
    chart.setOption({
        ...props.option,
    });
};

onBeforeUnmount(() => {
    chart?.dispose();
});
</script>

<style lang="scss" scoped>
.chart-container {
    margin: 2px;
    position: relative;
    // background-image: url('../../assets/img/line.png');
    background-color: #00080813;
    .title {
        font-size: 20px;
        border-bottom: 1px solid #ccc;
        box-sizing: border-box;
        width: min-content;
        white-space: nowrap;
        color: white;
        margin: 5px;
    }

    .my-chart {
        width: 100%;
        height: 100%;
    }

}




.boxfoot:before, .boxfoot:after {
    position: absolute;
    width: .5rem;
    height: .5rem;
    content: "";
    border-bottom: 2px solid #02a6b5;
    bottom: 0;
}
.boxall:before, .boxall:after {
    top: 0;
    position: absolute;
    width: .5rem;
    height: .5rem;
    content: "";
    border-top: 2px solid #02a6b5;
    bottom: 0;
}
.boxall:before, .boxfoot:before {
    border-left: 2px solid #02a6b5;
    left: 0;
}
.boxall:after, .boxfoot:after {
    border-right: 2px solid #02a6b5;
    right: 0;
}
</style>
