<template>
    <form :action="payment_url" method="POST">
        <input type="hidden" name="stripeToken" v-model="stripeToken">
        <input type="hidden" name="stripeEmail" v-model="stripeEmail">
        <button type="submit" class="btn btn-primary" :disabled="processing" @click.prevent="pay"><i v-show="processing" class="fa fa-refresh fa-spin fa-fw"></i>Confirm order and pay</button>
        <p class="help is-danger" v-show="status" v-text="status"></p>
    </form>
</template>

<script>
    export default {
        props: ['paymentkey', 'email', 'amount', 'paymenturl'],

        data() {
            return {
                stripeKey: this.paymentkey,
                customer_email: this.email,
                order_amount: this.amount * 100,
                payment_url: this.paymenturl,
                stripeEmail: '',
                stripeToken: '',
                status: false,
                processing: false,
                coupon: '',
            };
        },

        created() {
            this.stripe = StripeCheckout.configure({
                key: this.paymentkey,
                image: "https://stripe.com/img/documentation/checkout/marketplace.png",
                locale: "auto",
                panelLabel: "Payment",
                email: this.email,
                token: (token) => {
                    this.stripeToken = token.id;
                    this.stripeEmail = token.email;

                    axios.post(this.payment_url, { stripeToken: this.stripeToken, stripeEmail: this.stripeEmail, payment_method: 'stripe'})
                        .then(function(response){
                            console.log(response)
                            //alert('Complete! Thanks for your payment!');
                            this.status = response.data.status;
                            window.location.href = response.data.url;
                        }.bind(this));
                }
            });
        },

        methods: {
            pay() {
                this.processing = false;
                this.stripe.open({
                    name: 'Payment - Djangoshop',
                    description: '',
                    zipCode: false,
                    amount: this.order_amount,
                });
            }
        }
    }
</script>
