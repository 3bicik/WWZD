import './App.css';
import {useEffect, useState} from "react";
import {PolarArea} from "react-chartjs-2";
import axios from "axios";

import {Chart, registerables} from 'chart.js';

Chart.register(...registerables);

function App() {

    const [state, setState] = useState(null)
    const [selected, setSelected] = useState(0  )
    const [chartData, setChartData] = useState(null)

    const characters = [
        {
            id: 0,
            name: 'Character A',
            sentiment: {
                happy: 0.14,
                angry: 0.28,
                surprise: 0.54,
                sad: 0.12,
                fear: 0.32
            }
        },
        {
            id: 1,
            name: 'Character B',
            sentiment: {
                happy: 0.44,
                angry: 0.48,
                surprise: 0.14,
                sad: 0.15,
                fear: 0.12
            },
        },
        {
            id: 2,
            name: 'Character C',
            sentiment: {
                happy: 0.74,
                angry: 0.28,
                surprise: 0.34,
                sad: 0.05,
                fear: 0.22
            }
        },
    ]

    useEffect(() =>{
        axios.get('http://127.0.0.1:8000/app/characters/').then(res =>{
            console.log(res)
            setState(res.data)

            }
        )
        if(state && selected){
            console.log('1', state.filter(el => el.id = selected)[0].personality)
            setChartData(
            {
        labels: ['happy', 'angry', 'surprise', 'sad', 'fear'],
        datasets: [{
            label: '# of Votes',
            data: state.filter(el => el.id = selected)[0].personality,
            // data: [3,5,6,7,8],
            backgroundColor: [
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
                "rgba(255, 206, 86, 0.5)",
                "rgba(75, 192, 192, 0.5)",
                "rgba(153, 102, 255, 0.5)",
            ],
            borderWidth: 1,
        }]
    }
        )}
    },[selected])

    console.log(selected)

    return state ? (
        <div className="App">
            <div className='container'>
                <div className="row">
                    <div className='col list-characters'>
                        <div className="list-group">
                            {state.map((el) => {
                                return (<button type="button" key={el.id} onClick={() => setSelected(el.id)}
                                                className="list-group-item list-group-item-action align-self-center">
                                    {el.name}
                                </button>)
                            })}
                        </div>
                    </div>
                    <div className='col align-middle'>
                        {console.log('2', chartData)}
                        {chartData ? <PolarArea data={chartData}/> : null}
                    </div>
                </div>
            </div>
        </div>
    ) : null;
}

export default App;
