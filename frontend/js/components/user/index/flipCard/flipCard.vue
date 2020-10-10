<template>
    <div id="fliped" class='lax' data-lax-preset="spin fadeInOut">
        <div id="flipedWrapper" class="flipCardGlider">
            <card
                title="مرجوعی کالا"
                svg='/images/svg/box.svg'
            ></card>
            <card 
                title="تایید و کنترل کیفیت"
                svg='/images/svg/confirm.svg'
            ></card>
            <card 
                title="دسترسی به تامین کنندگان"
                svg='/images/svg/networking.svg'
            ></card>
            <card 
                title="گارانتی"
                svg='/images/svg/shield(1).svg'
            ></card>


            
        </div>
    </div>

</template>

<script>
    import card from './card.vue'

    export default{
        components:{
            card
        }
    }
</script>

<style scoped>
    #flipedWrapper{
        width:100%;
        display:flex;
      padding: 10px;
        justify-content: space-between;
        overflow-x:auto
    }
    #fliped{
        width:100%;
        display:flex;
        justify-content: center;
    
        margin-top:50px;
        background: #ffffff;
    }
    #flipedWrapper::-webkit-scrollbar {
  display: none;
    }


    #flipedWrapper {
    -ms-overflow-style: none; 
    scrollbar-width: none; 
    }
</style>