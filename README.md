# 奇幻大陆冒险游戏项目文档

## 项目结构

* **📜 README.md** - 项目说明文档

* **📦 requirements.txt** - 项目依赖清单

* **📁 assets** - 游戏资源

  * **🖼️ images** - 图像资源

    * \*.jpg 文件（日期格式命名）
    * 📜 README.md

  * **🔊 sounds** - 音效资源

    * 📜 README.md
    * **🗣️ manbo** - 角色音效
      * \*.wav 文件（日期格式命名）

* **⚙️ config** - 配置文件

  * 🔑 apikey.json
  * 📜 README.md

* **📚 docs** - 文档目录
  * 📜 README.md

* **💻 src** - 源代码

  * 🚀 main.py - 项目入口

  * 📜 README.md

  * 📖 story\_generation.py

  * **🧠 ai** - AI功能模块

    * **🎨 images** - 图像生成

      * image.py
      * image\_get.py
      * image\_post.py
      * 📜 README.md

    * **📝 prompts** - 提示模板

      * \*.txt 模板文件
      * load\_prompts.py

    * **🔊 sounds** - 语音合成

      * story\_tell.py
      * video\*.py

    * **📄 text** - 文本处理
      * vivo\_70B.py

    <!-- 其他子目录结构类似，此处省略 -->

## 依赖安装

```
pip install -r requirements.txt
    
```

## 使用说明

* 1\. 配置API密钥到 `config/apikey.json`
* 2\. 运行 `src/main.py` 启动游戏
* 3\. 在游戏界面中输入指令进行冒险

## 注意事项

* 确保API密钥有效且网络连接正常
* 资源文件命名采用 `YYYY_MM_DD_HH_MM_SS` 格式
* 建议定期清理生成的历史记录文件
