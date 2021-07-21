<script>
   export let breach;
</script>


      <h3>{breach.Name}</h3>
      <img src={breach.LogoPath} alt="">
      <p>{@html breach.Description }</p>
      <p>{breach.PwnCount} accounts were compromised.</p>


<style>
   img {
      width: 100px;
   }
</style>