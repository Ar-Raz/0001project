<template>
    <div id="categoryName">
        <div id="categoryNameWrapper">
            <div id="categoryNameWrapper" class="inputs">
                <div class='formInputsWrapper'>
                        <input autocomplete="off" name="categoryName" @blur='focusOut($event)' class='inputWithLabelThatShouldStay signupFormInputs' id='categoryNameInput' type="text">
                        <label class='comeUpLabel' for="categoryNameInput">نامه دسته بندی</label>                                                                  
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {keepStay} from "../../mixIns/keepStay"

export default {
    mixins:['keepStay']
}
</script>