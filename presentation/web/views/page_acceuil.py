class Page_acceuil():

    def generer_page_acceuil(self):
        html = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Page_acceuil</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
          </head>
          <body>
          <section class="section">
            <div class="container">
              <h1 class="title">Application FFR</h1>
              <form class="box">
                <div class="field">
                  <label class="label">Email</label>
                  <div class="control">
                    <input class="input" type="email" placeholder="e.g. alex@example.com">
                  </div>
                </div>
    
                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input class="input" type="password" placeholder="********">
                  </div>
                </div>
    
                <button class="button is-primary">Sign in</button>
              </form>
            </div>
          </section>
          </body>
        </html>
        """
        return html





