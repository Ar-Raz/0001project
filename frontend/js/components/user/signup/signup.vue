<template>
  <div id="signup" class='shouldCollapse'>

    <div id="signupwrapper">
      <form action="">
        <div id="steps">
          <div class="step">
            <p>:نام</p>
            <div class="bullet">
                1
            </div>
            <div class="check"></div>
          </div>
        </div>
      </form>
    </div>

  </div>

</template>

<style scoped>
#steps{
  display: flex;
}
.bullet{
  padding: 5px;
  border: 1px solid black;
  border-radius: 50%;
}
</style>


<script>
import {validationRules} from "../mixIns/validationMixIn.js"
import {keepStay} from "../mixIns/keepStay.js"
export default{
}
</script>