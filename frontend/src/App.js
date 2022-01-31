import './App.css';
import {useEffect, useState} from "react";
import {PolarArea} from "react-chartjs-2";
import axios from "axios";
import Chart from 'react-apexcharts'

// import {Chart, registerables} from 'chart.js';

// Chart.register(...registerables);

function App() {

    const [state, setState] = useState([])
    const [currentEpisode, setCurrentEpisode] = useState("s01e01")
    // const [arr, setArr] = useState(null)
    // const [xMin, setXMin] = useState(100)
    // const [xMax, setXMax] = useState(-100)
    // const [yMin, setYMin] = useState(100)
    // const [yMax, setYMax] = useState(-100)

    const labels = ["Happy", "Sad", "Love", "Anger"]
    const episodes = [
        's01e01',
        's01e02',
        's01e03',
        's01e04',
        's01e05',
        's01e06',
        's01e07',
        's01e08',
        's01e09',
        's01e010',
        's01e011',
        's01e012',
        's01e013',
    ]


    useEffect(() =>{
        axios.get(`http://127.0.0.1:8000/app/${currentEpisode}/`).then(res =>{
            console.log('from API to state ->', res.data)
            setState(res.data)
                    // series.push(res.data[0])
            }
        )

    },[currentEpisode])

    function parser(state){

        const result = state.map(el => {

            const arr = el.fields.data.replace('"', '').replace(' ', ',').replace('[', '').replace(']', '')
            return {
                name: el.fields.name,
                data: arr.split(',')
            }

        })

        console.log('result from function', result)
        // setArr(result)
        return result
    }

    function srcSelect(state){

        const elements = state.map(el => {
            return [`../imgs/${el.fields.name}.png`]
        })

        console.log('elements', elements)
        return elements
    }


    // function normalize(){
    //
    //     let xMin = 100
    //     let xMax = -100
    //     let yMin = 100
    //     let yMax = -100
    //
    //     for(let i=0; i<arr.length; i++){
    //         if(arr.data[0] > xMax){
    //             console.log('tutaj1?')
    //             xMax = arr.data[0]
    //         }else if(arr.data[0] < xMin){
    //             console.log('tutaj2?')
    //             xMin = arr.data[0]
    //         }
    //
    //         if(arr.data[1] > yMax){
    //             yMax = arr.data[1]
    //         }else if(arr.data[1] < yMin){
    //             yMin = arr.data[1]
    //         }
    //     }
    //
    //     // console.log('cvsdvasdvasd', xMin)
    //
    //     // setXMin(xMin)
    //     // setXMax(xMax)
    //     // setYMin(yMin)
    //     // setYMax(yMax)
    // }

    // arr && normalize()
    // console.log('1', xMin)
    // console.log('2', xMax)
    // console.log('3')
    // console.log('4')

        console.log({state})
        const chartSettings = {
        series: parser(state),
      options: {
        chart: {
          height: 600,
          type: 'scatter',
          animations: {
            enabled: false,
          },
          zoom: {
            enabled: true,
              // type: 'x',
              // autoScaleYaxis: true,
              // zoomedArea: {
              //   fill:{
              //       color: '#90CAF9',
              //       opacity: 0.4
              //   },
              //     stroke:{
              //       color: '#0D47A1',
              //         opacity: 0.4,
              //         width: 1
              //     }
              // }
          },
          toolbar: {
            show: true
          },
        },
        colors: ['#056BF6', '#D2376A'],
        xaxis: {
          tickAmount: 7,
            tickPlacement: 'on',
            range: 2,
          min: 0,
          max: 2,
          title: {
              text: '<- Sad ------- Happy ->'
          },
        },
        yaxis: {
          tickAmount: 7,
            tickPlacement: 'on',
            min: -0.18,
            max: 0.15,
            title: {
              text: '<- Angry ------- Loving ->'
            },
            crosshairs: {
              show: true
            }
        },
        markers: {
          size: 20
        },
        fill: {
          type: 'image',
          // opacity: 1,
          image: {
            src: srcSelect(state),
            width: 40,
            height: 40
          }
        },
        legend: {
          labels: {
            useSeriesColors: true
          },
          markers: {
            customHTML: [
              function() {
                return ''
              }, function() {
                return ''
              }
            ]
          }
        }
      },


    };


    return state ? (
        <div className="App">
            <div className='container'>
                <div className="row">
                    <div className='col-1 list-characters'>
                        <div className="list-group">
                            {episodes.map((el) => {
                                return (<button type="button" key={el.id} onClick={() => setCurrentEpisode(el)}
                                                className="list-group-item list-group-item-action align-self-center">
                                    {el}
                                </button>)
                            })}
                        </div>
                    </div>
                    <div className='col align-middle'>
                        <Chart options={chartSettings.options} series={chartSettings.series} type="scatter" height={900}/>
                        {/*{console.log('2', chartData)}*/}
                        {/*{chartData ? <PolarArea data={chartData}/> : null}*/}
                    </div>
                </div>
            </div>
        </div>
    ) : null;
}

export default App;
