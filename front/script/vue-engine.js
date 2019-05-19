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
                    .get('/api/menu/proposal')
                    .then(response => {
                        this.menu = response.data._source;
                        this.error = false;
                    })
                    .catch(error => {
                        console.error(error);
                        this.error = true;
                    })
                    .finally(() => {
                        this.loading = false;
                    });
            }
        },
        mounted: function () {
            this.propose();
        },
    })
});
