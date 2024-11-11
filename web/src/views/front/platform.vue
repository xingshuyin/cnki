<template>
  <div class="index dark">
    <div class="title">
      <t-time style="position: absolute;left: 10px; top: 10px;"></t-time>
      <span>国家大平台系统综合数据分析</span>
      <!-- <linedo style="position: absolute;left: 50%; top: 10px; transform: translateX(-50%); width: 700px;">
        <span>马少平</span>学者画像 CNKI
      </linedo> -->
      <div style="position: absolute;right: 10px; top: 10px; font-size: 15px;display: flex;">
        <div>欢迎您: <span style="color: yellow;">{{ attrs.userinfo.username }}</span></div>
      </div>
    </div>
    <div class="content">
      <div class="column-left column">
        <div class="left-row" style="display: flex;flex-direction: column;">
          <chart :option="option_area_count" style="width: 100%;height: 100%;" title="地区占比"></chart>
        </div>
        <div class="left-row" style="display: flex;flex-direction: column;">
          <chart :option="option_domain" style="width: 100%;height: 100%;" title="相关领域"></chart>
        </div>
        <div class="left-row"
          style="overflow: auto;min-height: 0; display: flex; flex-direction: column;;background-color: #2c2c2c44;">
          <titlebar> 各省平台数 </titlebar>
          <t-scrolltable :data="[
            { name: '北京', count: 193 },
            { name: '天津', count: 164 },
            { name: '河北', count: 126 },
            { name: '山西', count: 102 },
            { name: '内蒙古', count: 94 },
            { name: '辽宁', count: 70 },
            { name: '吉林', count: 60 },
            { name: '黑龙江', count: 40 },
            { name: '上海', count: 30 }]" :columus='[
              { key: "index", label: "序号", width: "30px", align: "center" },
              { key: "name", label: "省/市", flex: "1" },
              { key: "count", label: "数量", flex: "1", align: "center" }
            ]' style="flex: 1; width: 100%;">
          </t-scrolltable>
        </div>
      </div>
    <div class="column-center column">
      <div class="cards">
        <div class="card">
          <div class="card-name">国家平台</div>
          <div class="card-value">1300</div>
        </div>
        <div class="card">
          <div class="card-name">参与人员</div>
          <div class="card-value">127756</div>
        </div>
        <div class="card">
          <div class="card-name">科技成果</div>
          <div class="card-value">6547</div>
        </div>
        <div class="card">
          <div class="card-name">参与高校</div>
          <div class="card-value">456</div>
        </div>
        <div class="card">
          <div class="card-name">合作企业</div>
          <div class="card-value">4532</div>
        </div>
      </div>


    </div>
    <div class="column-right column">
      <div class="right-row">
        <chart :option="option_platform_count" style="width: 100%;height: 100%;" title="平台数量"></chart>
      </div>
      <div class="right-row" style="display: flex;flex-direction: column;">
        <titlebar> 平台名单 </titlebar>
        <t-scrolltable :data="
          [
            { 
              name:'国家水煤浆工程技术研究中心', uni:'炭科学技术研究有限公司',domain:'能源',url:'http://www.agriinfo.ac.cn/',
            },
            {
              name:'中国农业科学院农业信息研究所', uni:'中国农业科学院',domain:'农业',url:'http://www.agriinfo.ac.cn/',
            },
            {
              name:'中国农业科学院农业信息研究所', uni:'中国农业科学院',domain:'农业',url:'http://www.agriinfo.ac.cn/',
            }
          ]
        "
          :columus='[
            { key: "index", label: "序号", width: "30px", align: "center" },
            { key: "name", label: "标题", flex: "1", roll: true, url: (v) => v.url },
            { key: "domain", label: "领域", flex: "1", roll: true, url: (v) => v.url },
            { key: "uni", label: "依托单位", flex: "1", roll: true },
          ]' style="flex: 1; width: 100%;"></t-scrolltable>
      </div>
    </div>
  </div>
</div>


</template>
<script setup>
import { computed, onMounted, reactive } from 'vue';
import { useRouter } from 'vue-router';
import rest from '../../utils/rest';
import store from '../../store';
import result from './journals.json'
import { color } from 'echarts/core';
import linedo from '../../components/decoration/line.vue'
const router = useRouter()
const attrs = reactive({
  userinfo: {},
})

store().get_userinfo().then((info) => {
  attrs.userinfo = info
})


const click_to_url = (e) => {
  console.log(e)
  if (e.componentType == 'series' && e.data.url) { window.open(e.data.url) }
}


let option_area_count = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '基金分布',
    type: 'pie',
    barWidth: '60%',
    data: [
      { value: 1048, name: '西部地区' },
      { value: 735, name: '中部地区' },
      { value: 580, name: '东部地区' },
      { value: 484, name: '华北地区' },
      { value: 300, name: '华南地区' },

    ],
  }
};
let option_domain = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  xAxis: {
    type: 'category',
    data: ['生物医学工程', '计算机科学', '化学工程', '材料科学', '环境科学'],
    splitLine: {
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick: {
      show: false
    },
    axisLabel: {
      color: '#fff',
      interval: 0,
      rotate: 45,
    },
    axisPointer: {
      show: true,
    },

  },
  yAxis: {
    type: 'value',
    splitLine: {
      show: false
    },
    axisLabel: {
      color: '#fff'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '相关领域',
    type: 'bar',
    barWidth: '60%',
    data: [37, 26, 59, 48, 98],
  }
}

let option_platform_count  = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  xAxis: {
    type: 'category',
    data: ['国家重点实验室', '国家工程技术研究中心', '国家重大科技专项', '国家重点研发计划', '国家技术创新中心'],
    splitLine: {
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick: {
      show: false
    },
    axisLabel: {
      color: '#fff',
      interval: 0,
      rotate: 45,
    },
    axisPointer: {
      show: true,
    },

  },
  yAxis: {
    type: 'value',
    splitLine: {
      show: false
    },
    axisLabel: {
      color: '#fff'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '平台数量',
    type: 'bar',
    barWidth: '60%',
    data: [37, 26, 59, 48, 98],
  }
}





















let option_author = computed(() => {

  let nodes = []
  let links = []
  let max_value = 0
  for (const i of result.subject_count['中国']) {
    nodes.push({
      id: i.name,
      name: i.name.split(',')[0],
      value: i.value,
      "symbolSize": i.value,
      "label": {
        "show": true
      },
    })
    max_value = Math.max(max_value, i.value)
  }

  let o = {
    visualMap: {
      type: 'continuous',
      max: max_value,
      outOfRange: {
        color: ['#121122', 'rgba(3,4,5,0.4)', 'red', 'blue'],
      }
    },
    tooltip: {
    },
    series: [
      {
        type: 'graph',
        layout: 'force',
        animation: false,
        zoom: 5,
        legendHoverLink: false,
        // emphasis: { //隐藏其他节点
        //   focus: 'adjacency',
        //   lineStyle: {
        //     width: 4
        //   }
        // },
        label: {
          formatter: '{b}',
          color: 'white',
        },
        // itemStyle: {
        //   color: 'white',
        // },
        roam: true,
        draggable: true,
        data: nodes,
        force: {
          edgeLength: 3,
          repulsion: 10,
          gravity: 0.8
        },
        links: links
      }
    ]
  };
  return o
})


let option_pub = {
  tooltip: {},
  xAxis: {
    type: 'category',
    data: result.subject_count['年度'].sort((v1, v2) => parseFloat(v1.name.slice(0, 4)) - v2.name.slice(0, 4)).map((v) => v.name),
    splitLine: {
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick: {
      show: false
    },
    axisLabel: {
      color: '#fff'
    },
    axisPointer: {
      show: true,
    },

  },
  yAxis: {
    type: 'value',
    splitLine: {
      show: false
    },
    axisLabel: {
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
      data: result.subject_count['年度'].map((v) => v.value),
      type: 'line',
      smooth: true,
      symbol: 'none',
    }
  ]
};

let option_fund = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '基金分布',
    type: 'pie',
    barWidth: '60%',
    data: result.subject_count['基金'],
  }
}
let option_jg = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '机构分布',
    type: 'pie',
    barWidth: '60%',
    data: result.subject_count['机构'],
  }
}

let option_fund_bar = {
  tooltip: {
    // trigger: 'axis',
    // axisPointer: {
    //   type: 'shadow'
    // }
  },
  xAxis: {
    type: 'category',
    data: result.subject_count['基金'].map((v) => v.name),
    splitLine: {
      show: false
    },
    axisLine: {
      show: false
    },
    axisTick: {
      show: false
    },
    axisLabel: {
      color: '#fff',
      interval: 0,
      rotate: 45,
    },
    axisPointer: {
      show: true,
    },

  },
  yAxis: {
    type: 'value',
    splitLine: {
      show: false
    },
    axisLabel: {
      color: '#fff'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  label: {
    color: "#fff"
  },
  series: {
    name: '基金分布',
    type: 'bar',
    barWidth: '60%',
    data: result.subject_count['基金'].map((v) => v.value),
  }
}

</script>
<style scoped lang='scss'>
.index {
  height: 100%;
  width: 100%;
  background-image: url('../../assets//img/bg.jpg');
  overflow: hidden;


  .title {
    text-align: center;
    height: 50px;
    font-size: 35px;
    font-weight: 700;
    color: white;
    position: relative;
    // background-color: white;
  }

  .content {
    width: 100%;
    height: calc(100% - 51px);
    gap: 10px;
    display: flex;


    .column-left,
    .column-right {
      width: 25%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
    }


    .left-row {
      flex: 1;
    }

    .right-row {
      flex: 1;
      height: 33%;
    }

    .message {
      height: fit-content;
      max-height: 33%;

      .message-line {
        display: flex;
        flex-direction: row;
        align-items: center;

        .name {
          font-size: 16px;
          font-weight: 700;
        }

        .value {
          padding-left: 3px;
          font-size: 16px;
          color: #dad7d7;
        }
      }
    }

    .column-center {
      padding-top: 0px;
      width: 50%;
      position: relative;
      display: flex;
      flex-direction: column;


      .cards {
        margin: 20px 0;
        display: flex;
        // gap: 126px;
        /* 设置卡片间的间距 */
        justify-content: space-around;
        /* 居中显示 */
        padding: 5px;

        .card {
          position: relative;
          width: 120px;
          padding: 8px;
          border-radius: 15px;
          background: linear-gradient(135deg, #6b11cb6c, #25d1fc4d);
          color: #fff;
          text-align: center;
          overflow: hidden;
          // box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
          transition: transform 0.3s ease, box-shadow 0.3s ease;
          cursor: pointer;
        }

        .card:hover {
          // transform: translateY(-10px) scale(1.05);
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }

        .card::before,
        .card::after {
          content: "";
          position: absolute;
          width: 200%;
          height: 200%;
          top: 50%;
          left: 50%;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.15);
          pointer-events: none;
          transition: transform 0.5s ease;
        }

        .card::before {
          transform: translate(-50%, -50%) scale(0);
        }

        .card:hover::before {
          transform: translate(-50%, -50%) scale(1);
        }

        .card-name {
          font-size: 20px;
          margin: 0;
          font-weight: bold;
          color: #ffffffc0;
          white-space: nowrap;
        }

        .card-value {
          font-size: 36px;
          font-weight: bold;
          margin: 0;
          color: #fff;
        }
      }

      .center-center {
        width: 100%;
        flex: 1;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;

        .header-img {
          position: absolute;
          left: 50%;
          top: 40%;
          z-index: 10;
          transform: translate(-50%, -50%);
          border: 10px solid #ffffff;
          border-radius: 50%;
          border-style: dashed;
        }

        .pointer {
          z-index: 5;
          background: radial-gradient(circle, #2215dba4, #2215dba4, #26292c9f, #343d448e, #6b6b70a4);
          width: 90px;
          height: 90px;
          display: flex;
          justify-content: center;
          align-items: center;
          white-space: nowrap;
          border: 5px solid #ffffff98;
          border-radius: 50%;
          border-style: dashed;
          position: absolute;
          font-size: 15px;
          /* 控制距离图片的距离，可以调整百分比 */
          // transform: rotate(var(--angle)) translate(200px) rotate(calc(var(--angle) * -1));
          /* 旋转到指定角度 */
          /* 添加样式 */
          // cursor: pointer;
          position: absolute;
          left: 50%;
          top: 47%;
        }

        .base {
          position: absolute;
          left: 50%;
          top: 30%;
          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
          transform: rotateX(70deg) translate(-50%, -50%);
          width: 750px;
          height: 580px;
          border-radius: 50%;
          background: radial-gradient(circle, #dedfe000, #ffffff00, #7d7f8100, #d4d8dbe7, #6b6e70a4);
        }
      }

      .center-bottom {
        width: 100%;
        height: 30%;
        display: flex;
        flex-direction: row;
      }
    }
  }
}
</style>
