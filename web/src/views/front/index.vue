<template>
  <div class="index dark">
    <div class="title">
      <t-time style="position: absolute;left: 10px; top: 10px;"></t-time>
      <span style="color: yellow;">马少平</span> <span style="color: yellow;">学者画像</span> <span>CNKI</span>
      <!-- <linedo style="position: absolute;left: 50%; top: 10px; transform: translateX(-50%); width: 700px;">
        <span>马少平</span>学者画像 CNKI
      </linedo> -->
      <div style="position: absolute;right: 10px; top: 10px; font-size: 15px;display: flex;">
        <div>欢迎您: <span style="color: yellow;">{{ attrs.userinfo.username }}</span></div>
      </div>
    </div>
    <div class="content">
      <div class="column-left column">
        <div class="left-row"
          style="overflow: auto;min-height: 0; display: flex; flex-direction: column;;background-color: #2c2c2c44; ">
          <titlebar> 学科分布 </titlebar>
          <div style="overflow: auto;min-height: 0; display: flex; flex-direction: column;padding: 10px 20px;">
            <div v-for="persent in Object.entries(result['subject_count_percent']['学科']) " :key="persent[0]">
              <div style="color: white; font-size: 16px;">{{ persent[0] }} {{
                result['subject_count_dict']['学科'][persent[0]] }}</div>
              <el-progress :percentage="persent[1]" color="#f56c6c" />
            </div>
          </div>
        </div>
        <div class="left-row">
          <chart v-for="o in search_author_options" :option="o" style="width: 100%;height: 100%;" title="合作作者"
            @click="click_to_url"></chart>
        </div>
        <div class="left-row rank" style="display: flex;flex-direction: column;">
          <titlebar> 最高下载TOP10 </titlebar>
          <t-scrolltable v-for="a in result['search_author_info']" :data="a['download_rank']" :columus='[
            { key: "index", label: "序号", width: "30px", align: "center" },
            { key: "title", label: "标题", flex: "1", roll: true, url: (v) => v.url },
            { key: "authors", label: "作者", flex: "1", shift: (v) => v.map(author => author.name).join("、"), roll: true },
            { key: "metrics", label: "下载", flex: "1", shift: (v) => v.DTC, align: "center" },
          ]' style="flex: 1; width: 100%;"></t-scrolltable>
        </div>
      </div>
      <div class="column-center column">
        <div class="user-card">
          <div class="header">
            <h2><a style="color: white;" :href="user.homepage">{{ user.name }}</a> </h2>
            <div :href="user.homepage" target="_blank" class="position">{{ user.position }}</div>
          </div>
          <p class="description">{{ user.description }}</p>
          <div class="info">
            <p><strong>电话：</strong>{{ user.phone }}</p>
            <p><strong>传真：</strong>{{ user.fax }}</p>
          </div>
        </div>
        <div class="cards">
          <div class="card">
            <div class="card-name">总发文量</div>
            <div class="card-value">{{ result['search_author_info'][0]['pub_count'] }}</div>
          </div>
          <div class="card">
            <div class="card-name">期刊发文量</div>
            <div class="card-value">{{ result['search_author_info'][0]['journal_count'] }}</div>
          </div>
          <div class="card">
            <div class="card-name">会议发文量</div>
            <div class="card-value">{{ result['search_author_info'][0]['meeting_count'] }}</div>
          </div>
        </div>

        <div class="domains">
          <div class="achieve">
            <titlebar> 研究项目 </titlebar>
            <p>下一代信息检索研究自然科学基金重点项目</p>
            <p>基于语义挖掘的智能搜索技术“863”项目</p>
            <p>基于内容的多媒体信息检索“973”项目二级课题</p>
            <p>智能信息处理的理论与方法自然科学基金优秀创新群体项目</p>

          </div>
          <chart :option="option_domains" style="width: 100%;height: 100%;background-color: unset;"
            @click="click_to_url"></chart>
          <div class="achieve">
            <titlebar> 研究成果 </titlebar>
            <p>国家科技进步二等奖1项HOCR-97综合集成汉字识别系统</p>
            <p>国家自然科学四等奖1项关于ARMA模型辨识与谐波恢复的研究</p>
            <p>国家科技进步三等奖1项地面军用智能机器人</p>
          </div>

        </div>
        <div class="center-theme">
          <chart :option="option_theme" style="width: 100%;height: 100%;" title="主题分布"></chart>
        </div>

      </div>
      <div class="column-right column">

        <div class="right-row">
          <chart :option="option_source" style="width: 100%;height: 100%;" title="来源分布"></chart>
        </div>
        <div class="right-row">
          <chart :option="option_fund" style="width: 100%;height: 100%;" title="基金分布"></chart>
        </div>
        <div class="right-row rank">
          <titlebar> 最高引用TOP10 </titlebar>
          <t-scrolltable v-for="a in result['search_author_info']" :data="a['quote_rank']" :columus='[
            { key: "index", label: "序号", width: "30px", align: "center" },
            { key: "title", label: "标题", flex: "1", roll: true, url: (v) => v.url },
            { key: "authors", label: "作者", flex: "1", shift: (v) => v.map(author => author.name).join("、"), roll: true },
            { key: "metrics", label: "引用", flex: "1", shift: (v) => v.CTC, align: "center" },
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
import result from './result.json'
import { color } from 'echarts/core';
import linedo from '../../components/decoration/line.vue'
const router = useRouter()
const attrs = reactive({
  userinfo: {},
})

let user = {
  name: "马少平",
  position: "清华大学计算机系教授-博士生导师",
  homepage: "http://www.thuir.cn/group/~msp/",
  description: "主要研究方向为智能信息处理和信息检索。现任中国人工智能学会会士、副理事长，中国中文信息学会副理事长。",
  phone: "010-627823191",
  fax: "010-62782266",
}
store().get_userinfo().then((info) => {
  attrs.userinfo = info
})


const click_to_url = (e) => {
  console.log(e)
  if (e.componentType == 'series' && e.data.url) { window.open(e.data.url) }
}

const search_author_options = computed(() => {
  let options = []
  result.search_author_info.forEach(author => {
    let option_relation = {
      tooltip: {
        formatter: (params) => {
          if (params.dataType == "edge") {
            return params.data.source + '->' + params.data.target
          }
          else {
            return params.data.name + ' PUC:' + params.data.PUC + ' DTC:' + params.data.DTC + ' CTC:' + params.data.CTC
          }
        }
      },
      // visualMap: {
      //   type: 'continuous',
      // },
      series: [
        {
          type: 'graph',
          layout: 'force',
          animation: false,
          zoom: 5,
          legendHoverLink: false,
          emphasis: { //隐藏其他节点
            focus: 'adjacency',
            lineStyle: {
              width: 10
            }
          },
          label: {
            formatter: '{b}',
            color: 'white',
          },
          roam: true,
          draggable: true,
          data: author.coauthors_nodes,
          force: {
            edgeLength: 5,
            repulsion: 10,
            gravity: 0.02
          },
          links: author.coauthors_links
        }
      ]
    };
    options.push(option_relation)
  });
  return options
})



// 研究领域
let domains_nodes = [
  {
    id: result.search_author_info[0].author.name,
    name: result.search_author_info[0].author.name,
    value: 100,
    "symbolSize": 35,
    // "label": {
    //   "show": true
    // },
    symbol: 'image://media/img/author.png',
  },
]
let domains_links = []
result.search_author_info[0].domains.forEach(i => {
  domains_nodes.push({
    name: i.name, value: i.value, "label": {
      "show": true
    },
    url: i.url,
  })
  domains_links.push({ source: result.search_author_info[0].author.name, target: i.name })

});

let option_domains = {
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
      roam: true,
      draggable: true,
      data: domains_nodes,
      force: {
        edgeLength: 21,
        repulsion: 15,
        gravity: 0.1
      },
      links: domains_links
    }
  ]
};

let option_theme = {
  tooltip: {},
  xAxis: {
    type: 'category',
    data: result.subject_count['主要主题'].map((v) => v.name),
    splitLine: { //图中纵向网格线
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
    splitLine: {  //图中横向网格线
      show: false
    },
    axisLabel: {
      color: '#fff'
    }
  },
  series: [
    {
      data: result.subject_count['主要主题'].map((v) => v.value),
      type: 'bar',
      itemStyle: {
        borderRadius: 3,
      },
      label: {
        show: true,
        position: 'top',
        color: '#fff'
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
      data: [820, 932, 901, 934, 1290, 1330, 1320],
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


let option_source = {
  tooltip: {
    trigger: 'item'
  },
  series: [
    {
      name: '来源分布',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        // borderRadius: 10,
        // borderColor: '#fff',
        // borderWidth: 2
      },

      legend: {
        orient: 'vertical',
        left: 'left',
        textStyle: {
          color: '#fff'
        },
        borderColor: '#ffffff00',
        borderWidth: 0,
      },
      label: {
        color: "#fff"
      },
      borderWidth: 0,
      // emphasis: {
      //   label: {
      //     show: true,
      //     fontSize: 40,
      //     fontWeight: 'bold'
      //   }
      // },
      labelLine: {
        show: true
      },
      data: result['subject_count']['文献来源']
    }
  ]
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
    }


    .left-row {
      height: 30%;
    }

    .right-row {
      height: 30%;
    }

    .column-center {
      padding-top: 0px;
      width: 50%;
      position: relative;
      display: flex;
      flex-direction: column;

      .user-card {
        width: 99%;
        margin: 0 auto;
        padding: 5px;
        border-radius: 5px;
        background: linear-gradient(135deg, #4a91e252, #50e3c33b);
        color: #ffffff;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        text-align: center;

        .header h2 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
        }

        .position {
          display: block;
          font-size: 16px;
          color: #e0e0e0;
          margin-bottom: 10px;
        }

        .homepage-link {
          color: #ffffff;
          text-decoration: underline;
          font-size: 14px;
          display: inline-block;
          margin-top: 5px;
          transition: color 0.2s ease;
        }

        .homepage-link:hover {
          color: #ffeb3b;
        }

        .description {
          font-size: 16px;
          margin: 10px 0;
          line-height: 1.5;
        }

        .info {
          font-size: 14px;
          line-height: 1.5;
          height: 80%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          gap: 20px;
        }

        .info p {
          margin: 5px 0;
        }

        .info strong {
          color: #ffeb3b;
        }
      }

      .user-card:hover {
        // transform: translateY(-10px) scale(1.05);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
      }

      .cards {
        margin: 20px 0;
        display: flex;
        gap: 126px;
        /* 设置卡片间的间距 */
        justify-content: center;
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
        }

        .card-value {
          font-size: 36px;
          font-weight: bold;
          margin: 0;
          color: #fff;
        }
      }

      .domains {
        flex: 1;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-around;
        overflow: hidden;

        .achieve {
          height: 100%;
          width: 200px;
          font-size: 15px;
          overflow: auto;

          p {
            padding: 5px;
          }
        }
      }


      .center-theme {
        width: 100%;
        height: 25%;
      }
    }
  }
}
</style>
