<template>
  <div>
    <form novalidate @submit.prevent="userRegister">
      <div v-show="step === 1">

        <div v-if="regMessage" class="alert alert-success" role="alert">
          Вы успешно зарегистрировались!
        </div>

        <div class="form-group">
          <label for="name">Ваше имя</label>

          <input id="name"
                 v-model.trim="formReg.name"
                 :class="status($v.formReg.name)"
                 class="form-control" type="text" @blur="$v.formReg.name.$touch()">

          <div v-if="!$v.formReg.name.required" class="invalid-feedback">{{ reqText }}</div>
          <div v-if="!$v.formReg.name.alpha" class="invalid-feedback">{{ alphaText }}</div>
        </div>

        <div class="form-group">
          <label for="surname">Ваша фамилия</label>

          <input id="surname"
                 v-model.trim="formReg.surname"
                 :class="status($v.formReg.surname)"
                 class="form-control" type="text" @blur="$v.formReg.surname.$touch()">

          <div v-if="!$v.formReg.surname.required" class="invalid-feedback">{{ reqText }}</div>
          <div v-if="!$v.formReg.surname.alpha" class="invalid-feedback">{{ alphaText }}</div>
        </div>

        <div class="form-group">
          <label for="email">Email</label>

          <input id="email"
                 v-model.trim="formReg.email"
                 :class="status($v.formReg.email)"
                 class="form-control" type="text" @blur="$v.formReg.email.$touch()">

          <div v-if="!$v.formReg.email.required" class="invalid-feedback">{{ reqText }}</div>
          <div v-if="!$v.formReg.email.email" class="invalid-feedback">Пожалуйста введите Email адрес</div>
        </div>

        <div class="form-group">
          <label for="year">Год рождения</label>

          <select id="year"
                  v-model="formReg.year"
                  :class="status($v.formReg.year)"
                  class="custom-select" @blur="$v.formReg.year.$touch()">
            <option disabled value="">Выберите</option>
            <option v-for="(year, index) in years"
                    :key="index"
                    :value="year">{{ year }}
            </option>
          </select>

          <div v-if="!$v.formReg.year.required" class="invalid-feedback">{{ reqText }}</div>
        </div>

        <button :disabled="disabledBtn" class="btn btn-primary"
                type="button" @click="step++">Следующий шаг
        </button>

      </div>

      <transition name="slide-fade">
        <div v-show="step === 2">

          <div class="form-group">
            <label for="career">Профессия</label>

            <input id="career"
                   v-model.trim="formReg.career"
                   :class="status($v.formReg.career)"
                   class="form-control" placeholder="Например, Frontend"
                   type="text" @blur="$v.formReg.career.$touch()">

            <div v-if="!$v.formReg.career.alpha" class="invalid-feedback">{{ alphaText }}</div>
          </div>

          <div class="form-group">
            <label for="career">Описание</label>

            <b-textarea v-model="formReg.textarea"
                        :class="status($v.formReg.textarea)"
                        placeholder="О себе"
                        type="text" @blur="$v.formReg.textarea.$touch()"/>

            <div v-if="!$v.formReg.textarea.required" class="invalid-feedback">{{ reqText }}</div>
          </div>

          <div class="form-group">
            <label for="password">Пароль</label>

            <input id="password"
                   v-model.trim="formReg.password"
                   :class="status($v.formReg.password)"
                   class="form-control" type="text" @blur="$v.formReg.password.$touch()">

            <div v-if="!$v.formReg.password.required" class="invalid-feedback">{{ reqText }}</div>
            <div v-if="!$v.formReg.password.minLength"
                 class="invalid-feedback">{{ minLengthText }}
            </div>
          </div>

          <div class="form-group">
            <label for="passwordConfirm">Подтверждение пароля</label>

            <input id="passwordConfirm"
                   v-model.trim="formReg.passwordConfirm"
                   :class="status($v.formReg.passwordConfirm)"
                   class="form-control" type="text" @blur="$v.formReg.passwordConfirm.$touch()">

            <div v-if="!$v.formReg.passwordConfirm.sameAs"
                 class="invalid-feedback">{{ passwordConfirmText }}
            </div>
          </div>

          <button class="btn btn-light mr-2" type="button" @click="step--">Назад</button>
          <button :disabled="disabledBtnFinish"
                  class="btn btn-primary" type="submit">Зарегистрироваться
          </button>

        </div>
      </transition>
    </form>

  </div>

</template>

<script>
import {email, helpers, minLength, required, sameAs} from 'vuelidate/lib/validators'

const alpha = helpers.regex('alpha', /^[a-zA-Zа-яёА-ЯЁ]*$/)
export default {
  data() {
    return {
      step: 1,
      regMessage: false,
      years: [],
      yearEnd: 2020,
      reqText: 'Поле обязательно для заполнения',
      alphaText: 'Запрещены цифры, пробелы и другие символы',
      minLengthText: 'Минимальная длина 6 символов!',
      passwordConfirmText: 'Пароли не совпадают',
      formReg: {
        email: '',
        name: '',
        surname: '',
        year: '',
        career: '',
        textarea: '',
        password: '',
        passwordConfirm: ''
      }
    }
  },
  computed: {
    disabledBtn() {
      return this.$v.formReg.name.$invalid ||
          this.$v.formReg.surname.$invalid ||
          this.$v.formReg.email.$invalid ||
          this.$v.formReg.year.$invalid
    },
    disabledBtnFinish() {
      return this.$v.formReg.career.$invalid ||
          this.$v.formReg.textarea.$invalid ||
          this.$v.formReg.password.$invalid ||
          this.$v.formReg.passwordConfirm.$invalid
    }
  },
  methods: {
    status(validation) {
      return {
        'is-invalid': validation.$error,
        'error': validation.$error
      }
    },
    userRegister() {
      console.group("Form second")
      console.log('Вы успешно зарегистрированны!')
      console.log('Ваше имя: ' + this.formReg.name)
      console.log('Ваша фамилия: ' + this.formReg.surname)
      console.log('Email: ' + this.formReg.email)
      console.log('Год рождения: ' + this.formReg.year)
      console.log('Профессия: ' + this.formReg.career)
      console.log('Пароль: ' + this.formReg.password)
      console.groupEnd()
      this.reset()
    },
    reset() {
      // сбросить шаг и показать сообщение о регистрации
      this.step = 1;
      this.regMessage = true;
      // убрать сообщение о регистрации
      setTimeout(() => {
        this.regMessage = false
      }, 3000)
      // сбросить все поля
      for (let input in this.formReg) {
        this.formReg[input] = ''
      }
      // сбросить валидацию
      this.$v.$reset()
    }
  },
  validations: {
    formReg: {
      email: {
        email,
        required
      },
      name: {
        required,
        alpha
      },
      surname: {
        required,
        alpha
      },
      year: {
        required
      },
      career: {
        alpha
      },
      textarea: {
        required
      },
      password: {
        required,
        minLength: minLength(6)
      },
      passwordConfirm: {
        sameAs: sameAs('password')
      }
    }
  },
  created() {
    for (let i = this.yearEnd; i >= 1980; i--) this.years.push(i)
  }
}
</script>

<style scoped>
form {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 10px 10px 45px -31px rgba(0, 0, 0, 0.75);
}
</style>