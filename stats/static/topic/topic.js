var ctx = document.getElementById("myChart").getContext("2d");

var data = [
    {
        value: parseInt(document.getElementById('yes').innerHTML),
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "Yes"
    },
    {
        value: parseInt(document.getElementById('no').innerHTML),
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "No"
    },
];

var myPieChart = new Chart(ctx).Pie(data);