<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Prisotnost</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
</head>

<body>

  <section class="hero is-success is-fullheight">

    <div class="hero-head">
      <header class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <span class="navbar-burger" data-target="navbarMenuHeroC">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
          <div id="navbarMenuHeroC" class="navbar-menu">
            <div class="navbar-end">
              <a class="navbar-item is-active" href="/">
                Domov
              </a>
              <a class="navbar-item" href="/udelezenci/">
                Udeleženci
              </a>
              <a class="navbar-item" href="/dogodki/">
                Dogodki
              </a>
              <span class="navbar-item">
                <a class="button is-success is-inverted" href="https://github.com/miklaviclenart/prisotnost"
                  target="_blank" rel="noopener noreferrer">
                  <span class="icon">
                    <i class="fab fa-github"></i>
                  </span>
                  <span>Prenesi</span>
                </a>
              </span>
            </div>
          </div>
        </div>
      </header>
    </div>


    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title">
          Prisotnost
        </p>
        <p class="subtitle">
          Kdo je tu in kdo ne?
        </p>
      </div>
    </div>


    <div class="hero-foot">
      <nav class="tabs is-boxed is-fullwidth">
        <div class="container">
          <ul>
            <li><a href="/dodaj_udelezenca/">Dodaj udeleženca</a></li>
            <li><a href="/dodaj_dogodek/">Dodaj dogodek</a></li>
            <li><a href="/analiza/">Analiziraj</a></li>
          </ul>
        </div>
      </nav>
    </div>
  </section>

  <!-- <footer class='footer'>© 2021, Lenart Miklavič</footer> -->

</body>

</html>