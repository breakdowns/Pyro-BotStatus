name: Update Status

on:
  schedule:
    - cron: "0 */3 * * *"
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Clone Repo
        uses: actions/checkout@master
        with:
          repository: ${{ secrets.REPO_NAME }}
      - name: Install dependencies.
        run: |
          pip install pyrogram tgcrypto pytz==2021.3
          pip install --upgrade pip
      - name: Run the UserClient
        run: |
          python3 bot.py
        env:
          API_ID: ${{ secrets.API_ID }}
          API_HASH: ${{ secrets.API_HASH }}
          SESSION_STRING: ${{ secrets.SESSION_STRING }}
          BOT_LIST: "breakdownsmirror_bot slammingmirror_bot Breakdownsdc1bot breakdownsmltb_bot Breakdownstickerbot"
          CHANNEL_OR_GROUP_ID: ${{ secrets.CHANNEL_OR_GROUP_ID }}
          MESSAGE_ID: ${{ secrets.MESSAGE_ID }}
          BOT_ADMIN_IDS: ${{ secrets.BOT_ADMIN_IDS }}
          TIME_ZONE: "Asia/Jakarta"
          TIME_FORMAT: "%A, %d %B %Y - %H:%M:%S WIB"