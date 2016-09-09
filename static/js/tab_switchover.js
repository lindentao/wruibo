function showTab(num){
for (i=0; i<3; i++)
{
document.getElementById("tab"+i).style.display="none";
document.getElementById("id"+i).className="white";

}
document.getElementById("tab"+num).style.display="block";
document.getElementById("id"+num).className="blue";
}
