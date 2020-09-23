<template>
    <div id="productDesc">
        <div v-html="product.description"></div>
    </div>
</template>

<style>
    #productDesc{
        margin-bottom:20px;
    }
    #productDesc p {
        padding:10px;
        text-align: center;
    }

</style>

<script>
export default{
    props:['product'],
    mounted(){
        console.log('descs',this.product)
    }
}

</script>