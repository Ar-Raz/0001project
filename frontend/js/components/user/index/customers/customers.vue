<template>
        <div id="customers">
            <div id="customersWrapper">
                <div class="title">
                    <p>مشتریان ما</p>
                </div>
              <div class="swiper-container">
                <div class="swiper-wrapper">
                  <div class="swiper-slide">
                    <img alt="گلرنگ" title="گلرنگ" src="/images/ours1.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="شرکت نفتت" title="شرکت نفتت" src="/images/ours2.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="سایپا" title="سایپا" src="/images/ours3.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="شیرین عسل" title="شیرین عسل" src="/images/ours4.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/ours5.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/pakshoo.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/pishgaman.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/delveseh.png" >
                  </div>
                  <div class="swiper-slide">
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/mina.png" >
                  </div>
                </div>
                <!-- Add Arrows -->
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
              </div>
            </div>
        </div>

</template>

<script>
export default {
  mounted() {
    var swiper = new Swiper('.swiper-container', {
      slidesPerView: 3,
      loopAdditionalSlides:100,
      loop:true,
      spaceBetween: 30,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  }
}
</script>

<style scoped>
#customers{
    background: #ffffff;
    margin-top:50px;
}
#customersWrapper{
    display:flex;
    flex-direction:column;
    justify-content: center;
    padding: 10px;
  width: 100%;
}
.title p{
    text-align:center;
        font-size: 29px;
    font-weight: 800;
}
.cusImgs{
    display:flex;
    flex-wrap:wrap;
    justify-content: space-around;
}
.cusImgs img{
    filter:grayscale(1);
    width:200px;
    transition:all 0.4s;
  margin:10px;
}
@media (max-width:400px){
    .cusImgs{
        justify-content: center;
    }
}
@media (max-width: 425px)
{
  .cusImgs{
    justify-content: center;
  }
}
img:hover{
    filter:grayscale(0)
}
.swiper-container{
  width: 100%;
  margin-top:20px
}
.swiper-slide{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
}
.swiper-slide img{
  width: 200px;
  height: 200px;
}
</style>