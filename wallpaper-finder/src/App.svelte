<script>
  const unsplashUrl = "https://source.unsplash.com/";
  // https://source.unsplash.com/1600x900/?nature,water

  let reroll = 1;
  let loading = true;
  // let image;

  let keywords = "random";
  let width = window.screen.width * window.devicePixelRatio;
  let height = window.screen.height * window.devicePixelRatio;

  const getImage = async () => {};

  $: url = `${unsplashUrl}${width}x${height}/?${keywords.replace(/\s/, "")}`;
  $: url, (loading = true);
  $: url, (reroll = 0);
  // $: url, getImage(url);
</script>

<main class="columns">
  <div>
    <label class="label">Width</label>
    <input class="input" type="text" bind:value={width} />

    <label class="label">Height</label>
    <input class="input" type="text" bind:value={height} />

    <label class="label">Keywords (lorem, ipsum, ...)</label>
    <input class="input" type="text" bind:value={keywords} />

    <button
      class="button"
      class:is-loading={loading}
      on:click={() => {
        reroll++;
        loading = true;
      }}
    >
      Reroll #{reroll}
    </button>
  </div>

  <div class="column">
    <p>
      Generated url: {url}
    </p>
    <img
      src={url + "&reroll=" + reroll}
      alt="wallpaper"
      on:load={() => (loading = false)}
    />
  </div>
</main>

<style>
  main {
    margin: 2em;
  }
</style>
