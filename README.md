> **SPOG**: a **S**ingle **P**ane **O**f **G**lass for viewing data.

This repo contains a way to visualize the data in a browser.

## The data -- what is available?

* **[bugs.yaml](bugs.yaml)**
* **[stats.yaml](stats.yaml)**

## Viewing the data in your browser

* **[https://pages.github.com/stevemar/spog/](https://pages.github.com/stevemar/spog/)**: An online representation of the data.

## How's it work?

```bash
$ python3 generate_data.py
done generating YAML files
$ ./render.sh
+ which j2
+ j2 index.j2 bugs.yaml
+ j2 stats.j2 stats.yaml
$ open index.html
```

## Contributing

Submit an issue or PR.
