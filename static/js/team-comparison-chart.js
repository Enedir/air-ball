var statistic1 = statistics[0];
var statistic2 = statistics[1];

var comparison = document.getElementById("comparison");
if (statistic1 == null || statistic2 == null) {
    if (comparison != null)
        comparison.remove();
    
    throw new Error("The statistics haven't found!");
}

var aTeam1 = document.getElementById("team1-page");
var team1Name = document.getElementById("team1-name");

var aTeam2 = document.getElementById("team2-page");
var team2Name = document.getElementById("team2-name");

aTeam1.href = "../time?time=" + statistic1.fields.team[0];
team1Name.innerText = statistic1.fields.team[1];

aTeam2.href = "../time?time=" + statistic2.fields.team[0];
team2Name.innerText = statistic2.fields.team[1];

var categories = ['Vitórias', 'Derrotas',
                'PPG', 'RPG', 'APG', 'BPG', 'SPG',
                'TPG','FTP','FGP','TTP','Op. PPG'];
                
function setSelectOption(select, text) {
    for (var i = 0; i < select.options.length; i++) {
        if (select.options[i].text === text) {
            select.selectedIndex = i;
            break;
        }
    }
}

setSelectOption(document.getElementById("select1"), statistic1.fields.team[1]);
setSelectOption(document.getElementById("select2"), statistic2.fields.team[1]);

function createChart() {
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Comparação estatística'
        },
        subtitle: {
            text: 'Fonte dos dados: DataFodac'
        },
        xAxis: [{
            categories: categories,
            reversed: false,
            labels: {
                step: 1
            }
        }, { // mirror axis on right side
            opposite: true,
            reversed: false,
            categories: categories,
            linkedTo: 0,
            labels: {
                step: 1
            }
        }],
        yAxis: {
            title: {
                text: null
            },
            labels: {
                formatter: function () {
                    return Math.abs(this.value);
                }
            },
            tickPositioner: function () {
                
                var maxDeviation = Math.ceil(Math.max(Math.abs(this.dataMax), Math.abs(this.dataMin)));
                var halfMaxDeviation = Math.ceil(maxDeviation / 2);
        
                return [-maxDeviation, -halfMaxDeviation, 0, halfMaxDeviation, maxDeviation];
            }
        },

        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },

        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                this.point.category  + ': ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);
            }
        },

        series: [{
            name: statistic1.fields.team[1],
            data: [-statistic1.fields.wins,
                -statistic1.fields.loses,
                -statistic1.fields.ppg,
                -statistic1.fields.rpg,
                -statistic1.fields.apg,
                -statistic1.fields.bpg,
                -statistic1.fields.spg,
                -statistic1.fields.tpg,
                -statistic1.fields.ftp,
                -statistic1.fields.fgp,
                -statistic1.fields.ttp,
                -statistic1.fields.oppPts]
        }, {
            name: statistic2.fields.team[1],
            data: [ statistic2.fields.wins,
                statistic2.fields.loses,
                parseFloat(statistic2.fields.ppg),
                parseFloat(statistic2.fields.rpg),
                parseFloat(statistic2.fields.apg),
                parseFloat(statistic2.fields.bpg),
                parseFloat(statistic2.fields.spg),
                parseFloat(statistic2.fields.tpg),
                parseFloat(statistic2.fields.ftp),
                parseFloat(statistic2.fields.fgp),
                parseFloat(statistic2.fields.ttp),
                parseFloat(statistic2.fields.oppPts)]
        }]
    });
}

createChart();