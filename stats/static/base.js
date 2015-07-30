$(document).ready(function () {
   $.get('/api/country/all/', {}, function (data) {
       var injectCode = "";
       data = JSON.parse(data);
       if (data) {
           for (var i=0; i<data.length; ++i) {
               injectCode += "<a class='mdl-navigation__link' href='/country/" + data[i].fields.country_name + "'>" + data[i].fields.country_name + "</a>"
           }
       }
       else {
           injectCode = "<a class='mdl-navigation__link' href=''>No countries found</a>";
       }
       document.getElementById('nav-country-list').innerHTML = injectCode;
   }, "json") 
});