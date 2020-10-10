<template>
  <div id="aditionalInformation" class="productSection">
    <div class="creatProductTitle">
      <div class="createProductTitleWrapper">
        <svg
          style="
            height: 20px;
            transform: rotate(270deg);
            margin-right: 10px;
            cursor: pointer;
          "
          @click="toggleWrapperMethod($event)"
          viewBox="0 0 100 100"
        >
          <path
            d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z"
            class="arrow"
          ></path>
        </svg>
        <p>اطلاعات اضافی</p>
      </div>
    </div>
    <div class="hiddenAtDisPlay aditionalInformationWrapper">
      <div class="information">
        <div class="informationWrapper">
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>اصالت کالا</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="اصالت کالا" />
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>حداقل سفارش</label>
              </div>
              <div class="col2Input">
                <input
                  type="number"
                  name="product-minimum-order"
                  placeholder="حداقل تعداد"
                  min="1"
                />
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <p></p>
                <label for>روش پرداخت</label>
              </div>
              <div class="col1Input">
                <select name="product-payment-type">
                  <option value="چکی">چکی</option>
                  <option value="نقدی" selected>نقدی</option>
                </select>
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>وزن</label>
              </div>
              <div class="col2Input">
                <input type="number" placeholder="وزن" min="1" />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>کشور ساخت</label>
              </div>
              <div class="col1Input">
                <input
                  type="text"
                  name="product-made-in"
                  placeholder="کشور ساخت"
                />
              </div>
            </div>

            <div class="col2">
              <div class="col2Label">
                <label for>بازه اول قیمت</label>
              </div>
              <div class="col2Input">
                <input type="number" name="product-price" placeholder="بر حسب میلیون تومان" min="1" />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>جنس</label>
              </div>
              <div class="col1Input">
                <input type="text" placeholder="جنس" />
              </div>
            </div>
            <div class="col2">
              <div class="col2Label">
                <label for>بازه دوم قیمت</label>
              </div>
              <div class="col2Input">
                <input
                  name="product-price2"
                  type="number"
                  placeholder="بر حسب میلیون تومان"
                  min="1"
                />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>بسته بندی</label>
              </div>
              <div class="col1Input">
                <input
                  name="product-packing"
                  type="text"
                  placeholder="بسته بندی"
                />
              </div>
            </div>
            <div class="col2">
              <div class="col2Label">
                <label for>زمان تحویل</label>
              </div>
              <div class="col2Input">
                <input
                  name="product-delivery"
                  type="number"
                  placeholder="زمان ارسال بر حسب روز"
                  min="1"
                />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col1">
              <div class="col1Label">
                <label for>نمونه</label>
              </div>
              <div class="col1Input">
                <select name="product-samplaes" id="">
                  <option value="رایگان">رایگان</option>
                  <option value="اعمال هزینه">اعمال هزینه</option>
                  <option value="خیر" selected>خیر</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
label {
  display: flex;
}
#aditionalInformation {
  padding: 10px !important;
}
input {
  color: black;
  direction: rtl;
  border: 1px solid rgb(210, 214, 222);
  padding: 10px;
}
.col1Label,
.col2Label,
.col1Input,
.col2Input {
  width: 50%;
}
.col1Input input,
.col2Input input,
select {
  width: 250px;
}
.row {
  width: 100%;
  display: flex;
  margin-top: 20px;
  justify-content: flex-start;
}
.col1,
.col2 {
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.informationWrapper {
  margin-right: 30px;
}
.information {
  margin-top: 20px;
  margin-bottom: 20px;
}
.col1Label,
.col2Label {
  display: flex;
  justify-content: flex-end;
  margin-right: 10px;
}
.col1Input,
.col2Input {
  display: flex;
  justify-content: flex-end;
}
select{
  font-size: 14pt;
  direction: rtl;
}
@media (max-width: 880px) {
  .row {
    flex-direction: column;
  }
  .col1,
  .col2 {
    display: flex;
    width: 100%;
    flex-direction: column;
  }
  .col1 .col1Label,
  .col2 .col2Label,
  .col1 .col1Input,
  .col2 .col2Input {
    width: 100%;
  }
  .col1 .col1Label,
  .col2 .col2Label {
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .col1Input input,
  .col2Input input,
  select {
    width: 90%;
  }
}
</style>
