# github-to-gitea-mirror

Effortlessly synchronize your GitHub repositories to Gitea. `github-to-gitea-mirror` seamlessly detects GitHub repositories not present on Gitea and mirrors them, ensuring your repositories are consistent across both platforms.

## 🚀 Setup & Usage

1. Install required packages:
```bash
pip install python-dotenv requests
```

2. Create a `.env` file in your project directory with the following:
```bash
GITHUB_USER=your_github_username
GITEA_USER=your_gitea_username
GITEA_TOKEN=your_gitea_token
```

3. Run the script:
```bash
python your_script_name.py
```

## 🙌 Acknowledgements

- This script was developed with guidance from [Chat GPT](https://chat.openai.com/share/b62cabf7-ccc5-471f-89bc-7c272bbb4ec5).

## 🖋️ Author

**Kevin Veen-Birkenbach**
- 📧 [kevin@veen.world](mailto:kevin@veen.world)
- 🌐 [www.veen.world](https://www.veen.world/)

## 📜 License

Licensed under the GNU Affero General Public License v3.0. Please refer to the `LICENSE` file for complete details.