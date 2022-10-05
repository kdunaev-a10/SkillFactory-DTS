var app = new Vue({
    el: '#app',
    data: {
        loggedIn: false,
        loginFound: false,
        errors: [],
        form: {
            login: "",
            pass: ""
        },
        login: null,
        pass: null,
        user: null,
        creds: [{
                url: '/',
                login: "admin",
                pass: "LastJob",
                value: "WWEgb3N0YXZpbCBkbHlhIHRlYnlhIGZsYWcgdiBkaXJla3RvcmlpLCBhIHYga2Frb3ktIG5lIHNrYXpodS4gTG9naW4gdG90IHpoZSwgcGFzc3dvcmQ6IEFkbWlu"
            },
            {
                url: '/secret',
                login: "Admin",
                pass: "Admin",
                value: "flag*{I_AM*$UP3R_PRO_C00L_HAЦKER}"
            }
        ]
    },
    mounted() {

    },
    computed: {
        // form() {
        //     return {
        //         login: this.login,
        //         pass: this.form
        //     }
        // },
        detectUrl: function () {
            // this.creds.forEach(el => {
            //     if (el.login == this.login &&
            //         el.pass == this.pass)
            //         return el.url
            //     else return null
            // });
        },
        errorText: function () {
            return "everything OK"

            // switch (this.detectUrl) {
            //   case "/":
            //     return "Wrong Login";
            //     break;
            //     return "Wrong Password";
            //     break;
            // default: 
            // return null;
            // }
        }
    },
    methods: {
        doLogin() {
            this.errors = []
            console.log('form', this.form)
            if (!this.form.login) {
                this.errors.push("Введите логин")
            }

            if (!this.form.pass) {
                this.errors.push("Введите пароль")
            }

            this.creds.forEach((el, i, arr) => {
                console.log('el2', this.form)
                if (this.form.login == el.login &&
                    this.form.pass !== el.pass) {
                    this.errors.push("Wrong Password")
                    this.loginFound = true
                }
                if (this.form.login == el.login &&
                    this.form.pass == el.pass) {
                    this.user = el
                    this.loginFound = true
                }
            })
            if (this.loginFound == false)
                this.errors.push("Wrong login")

            if (this.errors.length == 0)
                this.loggedIn = !this.loggedIn
            // else alert("Заполните форму")
        },
        doLogout() {
            this.loggedIn = !this.loggedIn
        },
    }
})

  