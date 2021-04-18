const table1Btn = document.getElementById('load_data')
const table2Btn = document.getElementById('load_data1')
const table1 = document.querySelector('.table')
const clusterTable = document.querySelector('.cluster_table')

table1Btn.addEventListener('click', function(){
    table1.classList.toggle('active')
})

table2Btn.addEventListener('click', function(){
    clusterTable.classList.toggle('active')
})

