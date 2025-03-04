# GitHub to Gitea Mirror 🚀🔄
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)[![GitHub Stars](https://img.shields.io/github/stars/kevinveenbirkenbach/github-to-gitea-mirror)](https://github.com/kevinveenbirkenbach/github-to-gitea-mirror/stargazers)

**GitHub to Gitea Mirror** automatically detects repositories on GitHub that are not yet mirrored on Gitea and mirrors them—ensuring that your codebase remains consistent across both platforms.

## 🔧 Features

- **Auto-Detection:** Identifies GitHub repos missing on Gitea.
- **Seamless Mirroring:** Automatically mirrors repositories using the Gitea API.
- **Secure Authentication:** Utilizes environment variables and tokens for secure API access.

## 🚀 Installation

Install **GitHub to Gitea Mirror** via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager):

```bash
pkgman install gigimi
```

## 🛠️ Setup & Usage

1. **Install Required Packages:**

   If you haven't already, install the required Python packages:

   ```bash
   pip install python-dotenv requests
   ```

2. **Create a `.env` File:**

   In your project directory, create a `.env` file with the following content:

   ```bash
   GITHUB_USER=your_github_username
   GITEA_USER=your_gitea_username
   GITEA_TOKEN=your_gitea_token
   ```

3. **Run the Script:**

   Execute the script to start mirroring:

   ```bash
   python main.py
   ```

## 🙌 Acknowledgements

- Developed with guidance from [ChatGPT](https://chat.openai.com/).  
- Inspired by the need to maintain repository consistency across platforms.

## 🖋️ Author

**Kevin Veen-Birkenbach**  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)  
- 🌐 [https://www.veen.world/](https://www.veen.world/)

## 📜 License

This project is licensed under the GNU Affero General Public License v3.0. Please refer to the [LICENSE](./LICENSE) file for details.

---

Happy mirroring! 🎉🔄
