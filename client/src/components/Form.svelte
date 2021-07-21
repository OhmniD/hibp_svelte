<script>
    import { emailsStore, totalBreachesStore } from '../stores/stores.js'

    let email = ""

    const handleFormSubmit = async () => {
        let addEmail = await fetch(`http://localhost:8000/emails`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({"email":email})
		})
        const data = await addEmail.json()
        emailsStore.update(emails => [...emails, data])
        totalBreachesStore.update(n => n + data.num_of_breaches);
        email = ""
    };

</script>

<div id="form-wrapper">
    <form>
        <input type="text" name="email" bind:value={email} placeholder="Add an e-mail address">
        <button on:click|preventDefault={handleFormSubmit}>Add</button>
    </form>
</div>

<style>


    #form-wrapper {
        padding-top: 0.75rem;
        padding-right: 4rem;


    }

    input {
        border-radius: 0.25rem;
        width: 17rem;
    }

    button {
        border-radius: 0.25rem;
        margin-left: 1rem;
    }
</style>