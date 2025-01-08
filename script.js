document.querySelector("#page1").addEventListener("mousemove",function(dets){
    gsap.to("#page1 img",{
        x:`${dets.clientX * 0.02}px`,
        y:`${dets.clientY * 0.02}px`
    })
})
var typed = new Typed('.typed', {
    strings: ['Your Passport To Travel','Start Your Journey With Us'],
    typeSpeed: 50,
    smartBackspace: true,
  
    backSpeed: 70,
    loop:true
  });
// gsap.to("#main",{
//     scrollTrigger:{
//         trigger:"#page1",
//         start:"30% top",
//         scrub:1
//     },
//     backgroundColor:"white"
// })

document.querySelectorAll(".list h3").forEach(function(elem){
    elem.addEventListener("mouseover",function(){
        var index = elem.getAttribute("data-index")
        console.log(index);
        var percentage = -index * 100 + "%"
        // console.log();
        gsap.to(".image .img",{
            y:percentage
            // opacity:0
        })
    })
})
