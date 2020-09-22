<template>
	<div id="variations">
		<div id="variationsWraper">
			<div class="title">
				<p>اضافه کردن مشخصه فنی</p>
			</div>
			<div id="allVars">
				<div id="allVarsWrapper">
					<div id="vars" >

						

					</div>
					<div id="addVarButton">
						<button class="submit"  @click.prevent='addVar()'>اضافه کردن مشخصه فنی</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	
	export default{
		mounted(){
			this.vars=document.querySelector('#vars')
			let formData=new FormData()
			console.log(this.vars)
		},
		data(){
			return{
				vars:null,
				allVars:[{title}]
			}
		},
		methods:{
			addVar(){
				let templateLiteral=
				`
					<div class="singleVar">
						<button class='submit' @click="register">ثبت دسته بندی</button>
						<select>
							<option value="number">عددی</option>
							<option value="text">متنی</option>
						</select>
						<input type="text" placeholder="عنان مشخصه" :name="">
						
							
						</div>	
				`
				this.vars.insertAdjacentHTML("beforeend", templateLiteral)

			},
			register(){

			}
		}
	}
</script>

<style>
	
	#vars{
		display: flex;
		justify-content: center;
	}
</style>