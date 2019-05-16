$(document).ready(() => {
    let data = {
        menu: {
            name: null,
        },
        loading: true,
        error: false,
    };

    let vm = new Vue({
        el: '#app',
        data: data,
        methods: {
            propose: function () {
                this.loading = true;
                this.error = false;

                axios
                    .get('http://localhost/api/menu/proposal')
                    .then(response => {
                        this.menu = response.data._source;
                    })
                    .catch(error => {
                        console.error(error);
                        this.loading = false;
                        this.error = true;
                    })
                    .finally(() => {
                        this.loading = false;
                        this.error = false;
                    });
            }
        },
        mounted: function () {
            this.propose();
        },
    })
});
