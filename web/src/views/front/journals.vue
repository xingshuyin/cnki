<template>
  <div class="index dark">
    <div class="title">
      <t-time style="position: absolute;left: 10px; top: 10px;"></t-time>
      <span style="color: yellow;">马少平</span> <span style="color: yellow;">中文信息学报</span> <span>CNKI</span>
      <!-- <linedo style="position: absolute;left: 50%; top: 10px; transform: translateX(-50%); width: 700px;">
        <span>马少平</span>学者画像 CNKI
      </linedo> -->
      <div style="position: absolute;right: 10px; top: 10px; font-size: 15px;display: flex;">
        <div>欢迎您: <span style="color: yellow;">{{ attrs.userinfo.username }}</span></div>
      </div>
    </div>
    <div class="content">
      <div class="column-left column">

        <div class="left-row message" style="display: flex;flex-direction: column;">
          <titlebar> 基本信息 </titlebar>
          <div style="display: flex;flex-direction: row; align-items: center; flex: 1;overflow: hidden; padding: 5px;">
            <div class="cover" style="height: 100%;display: flex;justify-content: center;">
              <img class="" src="//c61.cnki.net/CJFD/big/MESS/MESS202409.jpg"
                onerror="this.src=AppPath+'/images/nopic1.gif'" alt="" id="pic-style1"
                style="overflow: hidden; z-index: 10; left: 15px; top: 0px; width: 120px; height: 166px;">
            </div>
            <div style="margin-left: 20px; height: 100%; overflow: auto;">
              <div class="message-line">
                <div class="name">主板单位: </div>
                <div class="value">中国中文信息学会</div>
              </div>
              <div class="message-line">
                <div class="name">出版周期: </div>
                <div class="value">月刊</div>
              </div>
              <div class="message-line">
                <div class="name">ISSN: </div>
                <div class="value">1003-0077</div>
              </div>
              <div class="message-line">
                <div class="name">CN: </div>
                <div class="value">11-2325/N</div>
              </div>
              <div class="message-line">
                <div class="name">出版地: </div>
                <div class="value">北京市</div>
              </div>
              <div class="message-line">
                <div class="name">语种: </div>
                <div class="value">中文;</div>
              </div>
              <div class="message-line">
                <div class="name">开本: </div>
                <div class="value">16开</div>
              </div>
              <div class="message-line">
                <div class="name">创刊时间: </div>
                <div class="value">1986</div>
              </div>


            </div>
          </div>
        </div>
        <div class="left-row rank" style="display: flex;flex-direction: column;">
          <chart :option="option_subject" style="width: 100%;height: 100%;" title="学科分布"></chart>
        </div>
        <div class="left-row"
          style="overflow: auto;min-height: 0; display: flex; flex-direction: column;;background-color: #2c2c2c44;">
          <titlebar> 主题分布 </titlebar>
          <div style="overflow: auto;min-height: 0; display: flex; flex-direction: column;padding: 10px 20px;">
            <div v-for="persent in Object.entries(result['subject_count_percent']['次要主题']) " :key="persent[0]">
              <div style="color: white; font-size: 16px;">{{ persent[0] }} {{
                result['subject_count_dict']['次要主题'][persent[0]] }}</div>
              <el-progress :percentage="persent[1]" color="#f56c6c" />
            </div>
          </div>
        </div>

      </div>
      <div class="column-center column">
        <div class="cards">
          <div class="card">
            <div class="card-name">总发文量</div>
            <div class="card-value">{{ result['articles'].length }}</div>
          </div>
          <div class="card">
            <div class="card-name">涉及主题</div>
            <div class="card-value">{{ result['subject_count']['主要主题'].length }}</div>
          </div>
          <div class="card">
            <div class="card-name">涉及学科</div>
            <div class="card-value">{{ result['subject_count']['学科'].length }}</div>
          </div>
          <div class="card">
            <div class="card-name">最高下载</div>
            <div class="card-value">{{ result['articles'].sort((a, b) => parseFloat(b.download) -
              parseFloat(a.download))[0].download }}</div>
          </div>
          <div class="card">
            <div class="card-name">最高被引</div>
            <div class="card-value">{{ result['articles'].sort((a, b) => parseFloat(b.quote) -
              parseFloat(a.quote))[0].quote }}</div>
          </div>
        </div>

        <div class="center-center">
          <img class="header-img" src="../../assets/img/author.png" alt="">

          <div class="pointer"
            style="--angle: 180deg;transform:  rotate(var(--angle)) translate(240px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            主题分布</div>
          <div class="pointer"
            style="--angle: 155deg;transform:  rotate(var(--angle)) translate(350px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            学科分布</div>
          <div class="pointer"
            style="--angle: 120deg;transform:  rotate(var(--angle)) translate(240px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            基金来源</div>


          <div class="pointer"
            style="--angle: 60deg;transform:  rotate(var(--angle)) translate(240px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            作者分布</div>
          <div class="pointer"
            style="--angle: 25deg;transform:  rotate(var(--angle)) translate(350px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            文献分析</div>
          <div class="pointer"
            style="--angle: 0deg;transform:  rotate(var(--angle)) translate(240px) rotate(calc(var(--angle) * -1)) translate(-50%, -50%);">
            发文趋势</div>

          <div class="base" style=""></div>
        </div>

        <div class="center-bottom">
          <chart :option="option_fund" style="width: 100%;height: 100%;" title="基金来源"></chart>
          <chart :option="option_author" style="width: 100%;height: 100%;" title="作者分布"></chart>
        </div>

      </div>
      <div class="column-right column">
        <div class="right-row">
          <chart :option="option_jg" style="width: 100%;height: 100%;" title="机构分布"></chart>
        </div>
        <div class="right-row">
          <chart :option="option_pub" style="width: 100%;height: 100%;" title="发文趋势"></chart>
        </div>
        <div class="right-row" style="display: flex;flex-direction: column;">
          <titlebar> 文献分析 </titlebar>
          <t-scrolltable :data="result['articles'].sort((a, b) => parseFloat(b.download) - parseFloat(a.download))"
            :columus='[
              { key: "index", label: "序号", width: "30px", align: "center" },
              { key: "title", label: "标题", flex: "1", roll: true, url: (v) => v.url },
              { key: "author", label: "作者", flex: "1", shift: (v) => v.join("、"), roll: true },
              { key: "download", label: "下载", flex: "1", align: "center" },
              { key: "quote", label: "引用", flex: "1", align: "center" },
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

let option_subject = {
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
    data: result.subject_count['学科'],
  }
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
      interval:0,
      rotate:45,
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
    data: result.subject_count['基金'].map((v) => v.value) ,
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
          width: 100px;
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
