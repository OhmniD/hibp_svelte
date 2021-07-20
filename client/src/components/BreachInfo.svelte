<script>
   export let breach;
</script>


      <h4>{breach.Name}</h4>
      <img src={breach.LogoPath} alt="">
      <p>{@html breach.Description }</p>


<style>
   img {
      width: 100px;
   }
</style>