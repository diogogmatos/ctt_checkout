# CTT Checkout

This tool first started as a C# Console Application made with Visual Studio even before I entered university. I was selling my old shcool books online
and I was having trouble knowing how much I should charge for shipping costs when sending them with CTT (the national post service), so I just made a
quick app to tell me just that. It started super simple, with just one shipping method, and slowly grew to a more complex thing.

Fast forward to today, I was learning Python and wanted something to practice, so I had the idea of converting my C# app. Well, I did
and it also turned more and more complex and now I'm invested in developing this little thing as I learn more about Python.

## What is CTT Checkout?

It's a simple terminal app written in Python that helps you know how much you'll need to pay for shipping to send your item with CTT.

<img align="left" width="500px" alt="Opening" src="https://github.com/sassypocoyo/ctt_checkout/blob/master/assets/picture.png?raw=true" />

## Features

- **Web Scraping**: Using the *BeautifulSoup* library, the program automatically fetches the latest shipping costs and other needed information from [ctt.pt](https://ctt.pt), so that the calculations are precise and always in sync with the company's prices;
- **Shipping Methods**: CTT Checkout currently supports *Correio Normal*, *Correio Azul* and *Correio Editorial*;
- **Packaging Options**: The main packaging options offered by CTT are implemented (Saquetas and Caixas), the corresponding weight and price of the selected package is added to the final cost;
- **Additional Services**: Optional services offered by CTT for each shipping method are implemented, this includes *Serviço Especial de Registo*, *Comprovativo de Entrega*, *Envio à Cobrança* and *Alertas por email e SMS*.

## Installing and running

On your Linux machine, make sure you have Python installed (obviously).

### Dependencies:

This program uses the *simple-term-menu*, *bs4* and *pandas* libraries, let's make sure you install them:

```bash
$ python -m pip install simple-term-menu
```

```bash
$ python -m pip install bs4
```

```bash
$ python -m pip install pandas
```
### Downloading and running:

Now let's clone the repository and move to it:

```bash
$ git clone https://github.com/sassypocoyo/ctt_checkout
$ cd ctt_checkout/src
```

Finally, let's compile/run it (use this everytime you want to run it):

```bash
$ python program_v2.0.py
```

## Developed by:

- [**Diogo Matos**](https://msha.ke/imdiogo)
