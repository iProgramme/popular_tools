当您创建一个代码项目时，编写一个详细的 `README.md` 文档可以帮助其他开发者更好地理解和使用您的代码。以下是一个示例 `README.md` 文档，根据您提供的代码内容编写的详细说明：

```markdown
# FindStars 数据抓取与统计工具

这个工具用于从 [FindStars](https://www.findstars.cn/search) 网站抓取数据并进行统计。它使用 Python 和 Selenium 进行网页抓取，使用 BeautifulSoup 进行数据解析，使用 Pandas 进行数据处理，最后将结果保存为 Excel 文件。

## 安装依赖

运行这个工具需要安装以下依赖库：

- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- Chrome 浏览器及对应的 ChromeDriver（请根据您的 Chrome 版本下载对应的 ChromeDriver）

您可以使用以下命令来安装这些依赖库：

```bash
pip3 install selenium beautifulsoup4 pandas
```

## 使用说明

1. 安装依赖库并下载对应版本的 ChromeDriver。
2. 打开代码中的 `chromedriver_path` 变量，将其设置为您下载的 ChromeDriver 的路径。
3. 运行代码：`python findstars_scraper.py`

程序将自动打开 Chrome 浏览器，访问 [FindStars](https://www.findstars.cn/search) 网站，并模拟滚动加载以获取前 100 个项目的数据。然后，它将访问每个项目的详细页面，提取文件大小，游戏人数，预估时间和MC评分的信息，并保存为 Excel 文件。

## 数据保存

抓取的数据将保存为一个 Excel 文件，文件名为 `data.xlsx`。

## 注意事项

- 确保您的 Chrome 浏览器版本与下载的 ChromeDriver 版本兼容。
- 请遵守网站的使用政策和法律法规，不要滥用此工具。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

希望这个文档对您理解和使用代码有所帮助。如果您有任何问题或建议，请随时联系我们。
```

这个 `README.md` 文档提供了工具的安装、使用说明，以及一些注意事项。您可以将其放在代码项目的根目录下，以帮助其他开发者更好地了解和使用您的代码。请根据实际情况对文档进行修改和补充。