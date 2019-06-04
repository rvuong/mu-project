$(document).ready(() => {
    let menuIndex = null;
    let menus = [];

    let data = {
        menu: {
            name: null,
        },
        user: null,
        loading: false,
        error: false,
    };


    // Creates the VueJS instance
    let vm = new Vue({
        el: '#app',
        data: data,
        methods: {
            authenticate: function () {
                // Fetches menus proposals
                axios
                    .get('/api/user')
                    .then(response => {
                        if (200 !== response.status) {
                            console.error(response.statusText);
                        } else {
                            this.user = response.data._source.name;
                        }
                    })
                    .catch(error => {
                        this.error = true;
                        console.error(error);
                    })
                ;
            },
            load: function () {
                this.loading = true;
                this.error = false;

                // Fetches menus proposals
                axios
                    .get('/api/menus')
                    .then(response => {
                        if (200 !== response.status) {
                            this.loading = false;
                            this.error = true;
                            console.error(response.statusText);
                        } else {
                            this.loading = false;
                            this.error = false;
                            menus = response.data.hits.hits.slice();
                        }
                    })
                    .catch(error => {
                        this.error = true;
                        console.error(error);
                    })
                    .finally(() => {
                        this.propose();
                    })
                ;
            },
            getRandomIndex: (max) => Math.floor(Math.random() * Math.floor(max)),
            propose: function () {
                let menuIndex = this.getRandomIndex(menus.length);

                this.menu = menus[menuIndex]._source;
            }
        },
        mounted: function () {
            this.authenticate();
            this.load();
        },
    })
});
