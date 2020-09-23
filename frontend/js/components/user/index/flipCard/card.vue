<template>
  <div class="flip-card">
      <div class="flip-card-front">
        <img :src='svg' />
        <p>{{title}}</p>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['svg',"title"]
  };
</script>
<style scoped>
.flip-card{
  margin:10px;
}
  .flip-card-front{
    display:flex;
    flex-direction:column;
    width:max-content;
    
    align-items: center;
    justify-content: space-between;

  }
  img{
    width:70px;
    height:70px;
  }
</style>