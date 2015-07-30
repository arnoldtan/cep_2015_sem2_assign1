$(document).ready(function () {
   var countries = document.getElementById('country_list_table').children[1].children;
   for (var i=0; i<countries.length; ++i) {
       var ans = countries[i].children;
       for (var j=1; j<ans.length; ++j) {
           if (ans[j].innerHTML === "True") ans[j].innerHTML = "Yes";
           else if (ans[j].innerHTML === "False") ans[j].innerHTML = "No";
       }
   }
});