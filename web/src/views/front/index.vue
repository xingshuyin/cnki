<template>
  <div class="index">
    <div class="title">
      大数据平台
    </div>
    <chart :option="option_relation" style="position: absolute; width: 100%; height: 100%"></chart>
    <div class="content">
      <div class="column">
        <chart :option="option"></chart>
        <chart :option="option_line"></chart>
        <chart :option="option"></chart>
      </div>

      <div class="column_m">
        <div></div>
        <div></div>
        
      </div>

      <div class="column">
        <chart :option="option" title="来源类别"></chart>
        <chart :option="option_line"></chart>
        <chart :option="option"></chart>
      </div>
    </div>
  </div>

</template>
<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import rest from '../../utils/rest';
import store from '../../store';
import author_data from './author_data.json'

let author = {}
for(let i = 0; i < author_data.detail.metadata.length; i++){
  author[author_data.detail.metadata[i].name] = author_data.detail.metadata[i].value
}

const author_relation = {
  nodes:[{
    id: author.CODE,
    name: author.NAME,
    value:  author_data.detail.metrics.reduce((a, b) => a + parseInt(b.value), 0),
    metrics: author_data.detail.metrics,
    url : author_data.detail.relations[0].url,
    symbolSize: 20,
    itemStyle: {
        color: 'red'
    }
  }],
  links:[]
}
for(let i = 0; i < author_data.coauthors.length; i++){
  let size = author_data.coauthors[i].metrics.reduce((a, b) => a + parseInt(b.value), 0)
  let metrics = author_data.coauthors[i].metrics
  let PUC = metrics.PUC
  let DTC = metrics.DTC
  let CTC = metrics.CTC
  author_relation.nodes.push({
    id: author_data.coauthors[i].id,
    name: author_data.coauthors[i].title,
    value: size,
    PUC:PUC,
    DTC:DTC,
    CTC:CTC,
    url : author_data.coauthors[i].relations[0].url,
    symbolSize: size/5000,
    itemStyle: {
        color: 'blue'
    }
  })
  author_relation.links.push({
    source: author.CODE,
    target: author_data.coauthors[i].id,
  })
}


const router = useRouter()
let option = {
  tooltip: {},
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    splitLine: { //图中纵向网格线
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick:{
      show: false
    },
    axisLabel:{
      color: '#fff'
    },
    axisPointer: {
      show: true,
    } ,
  },
  yAxis: {
    type: 'value',
    splitLine: {  //图中横向网格线
      show: false
    },
    axisLabel:{
      color: '#fff'
    }
  },
  series: [
    {
      data: [120, 200, 150, 80, 70, 110, 130],
      type: 'bar',
      itemStyle:{
        borderRadius: 3,
      },
      barWidth: '20%',
    }
  ],
  grid: { // 边距
    left: 40,
    right: 10,
    top: 10,
    bottom: 40,
    // show: false,
  }
};
let option_line = {
  tooltip: {},
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    splitLine: {
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick:{
      show: false
    },
    axisLabel:{
      color: '#fff'
    },
    axisPointer: {
      show: true,
    } ,

  },
  yAxis: {
    type: 'value',
    splitLine: {
      show: false
    },
    axisLabel:{
      color: '#fff'
    }
  },
  grid: {
    left: 40,
    right: 10,
    top: 10,
    bottom: 40,
    show: false,
  },
  series: [
    {
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: 'line',
      smooth: true,
      symbol: 'none',
    }
  ]
};

let option_relation = {
    // legend: {
    //   data: ['HTMLElement', 'WebGL', 'SVG', 'CSS', 'Other']
    // },
    series: [
      {
        type: 'graph',
        layout: 'force',
        animation: false,
        zoom:5,
        label: {
          position: 'right',
          formatter: '{b} PUC:{@PUC} DTC: {@DTC} CTC: {@CTC}',
          textBorderWidth :0,
          color: 'white',
        },
        roam: true,
        draggable: true,
        data: author_relation.nodes,
        force: {
          edgeLength: 5,
          repulsion: 20,
          gravity: 0.2
        },
        links: author_relation.links
      }
    ]
  };

</script>
<style scoped lang='scss'>
.index {
  height: 100%;
  width: 100%;
  background-image: url('../../assets//img/bg.jpg');
  display: flex;
  flex-direction: column;


  .title {
    text-align: center;
    height: 50px;
    font-size: 40px;
    color: white;
    // background-color: white;
  }

  .content {
    flex: 1;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-rows: 1fr;
    gap: 10px;

    .column {
      display: grid;
      grid-template-rows: repeat(3, 1fr);
      grid-template-columns: 1fr;
      gap: 10px;
    }

    .column_m {
      display: grid;
      grid-template-rows: 1fr 2fr;
      gap: 10px;
    }
  }
}
</style>
