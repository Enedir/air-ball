var statistic1 = statistics[0];
var statistic2 = statistics[1];

var comparison = document.getElementById("comparison");
if (statistic1 == null || statistic2 == null) {
    if (comparison != null)
        comparison.remove();
    
    throw new Error("The statistics haven't found!");
}

var aPlayer1 = document.getElementById("player1-page");
var aPlayer1Team = document.getElementById("player1-team-page");
var player1Name = document.getElementById("player1-name");
var player1Team = document.getElementById("player1-team");

var aPlayer2 = document.getElementById("player2-page");
var aPlayer2Team = document.getElementById("player2-team-page");
var player2Name = document.getElementById("player2-name");
var player2Team = document.getElementById("player2-team");

aPlayer1.href = "../jogador?jogador=" + statistic1.fields.player[0];
player1Name.innerText = "#" + statistic1.fields.player[2] + " " + statistic1.fields.player[1];
aPlayer1Team.href = "../time?time=" + statistic1.fields.player[0];
player1Team.innerText = statistic1.fields.player[4];

aPlayer2.href = "../jogador?jogador=" + statistic2.fields.player[0];
player2Name.innerText = "#" + statistic2.fields.player[2] + " " + statistic2.fields.player[1];
aPlayer2Team.href = "../time?time=" + statistic2.fields.player[0];
player2Team.innerText = statistic2.fields.player[4];
                
function setSelectOption(select, text) {
    for (var i = 0; i < select.options.length; i++) {
        if (select.options[i].text === text) {
            select.selectedIndex = i;
            break;
        }
    }
}

setSelectOption(document.getElementById("select1"), statistic1.fields.player[1]);
setSelectOption(document.getElementById("select2"), statistic2.fields.player[1]);

var categories = ['PPG', 'RPG', 'APG',
                'BPG', 'SPG', 'TPG', 'MPG', 'FTP', 'FGP',
                'TTP', 'FTM', 'FGM', 'TTM'];

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
            name: statistic1.fields.player[1],
            data: [-statistic1.fields.ppg,
                -statistic1.fields.rpg,
                -statistic1.fields.apg,
                -statistic1.fields.bpg,
                -statistic1.fields.spg,
                -statistic1.fields.tpg,
                -statistic1.fields.mpg,
                -statistic1.fields.ttp,
                -statistic1.fields.fgp,
                -statistic1.fields.ftp,
                -statistic1.fields.ftm,
                -statistic1.fields.fgm,
                -statistic1.fields.ttm]
        }, {
            name: statistic2.fields.player[1],
            data: [parseFloat(statistic2.fields.ppg),
                parseFloat(statistic2.fields.rpg),
                parseFloat(statistic2.fields.apg),
                parseFloat(statistic2.fields.bpg),
                parseFloat(statistic2.fields.spg),
                parseFloat(statistic2.fields.tpg),
                parseFloat(statistic2.fields.mpg),
                parseFloat(statistic2.fields.ttp),
                parseFloat(statistic2.fields.fgp),
                parseFloat(statistic2.fields.ftp),
                parseFloat(statistic2.fields.ftm),
                parseFloat(statistic2.fields.fgm),
                parseFloat(statistic2.fields.ttm)]
        }]
    });
}

createChart();