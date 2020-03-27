from flask import (
    Flask,
    current_app,
    g,
    session,
    request,
    render_template,
    jsonify,
    send_file,
    redirect,
    url_for,
)
from werkzeug.utils import secure_filename

# from pathUtility import basePath, curPath
from pathlib import Path


def isVideoFile(self):
    return self.suffix == ".mp4"


Path.isVideoFile = isVideoFile


curPath = Path("./")
basePath = Path("../")

import logging as log

log.basicConfig(level=log.DEBUG)
log.debug("this is a demo massage")

app = Flask(__name__)
# app.config["USE_X_SENDFILE"] = True


def sortedFileList(dirPath):
    """"just sort the dir or file order"""

    sortedList = []

    for path in dirPath.glob("*"):
        if path.is_dir():
            sortedList.insert(0, path)
        else:
            sortedList.append(path)

    if str(dirPath) != ".":
        sortedList.insert(0, dirPath / "../")

    return sortedList


@app.route("/")
def homepage():
    return redirect(url_for("testFolderView"))


@app.route("/testFolderView/", defaults={"var": "upside"})
@app.route("/testFolderView/<path:var>")
def testFolderView(var=""):
    intoPath = curPath / var
    log.debug((intoPath, basePath, var))
    # log.debug((intoPath.resolve(), basePath.resolve(), var))

    if intoPath.exists():
        if intoPath.is_dir():
            return render_template(
                "folderView.html",
                cwdUrl="/testFolderView/",
                childrens=sortedFileList(intoPath),
                resourceUrl="/resources/",
            )
        else:
            return render_template("video.html", cwdUrl="/resources/", item=intoPath)
    else:
        return render_template(
            "folderView.html", cwdUrl="/testFolderView/", childrens=["../"]
        )


@app.route("/resources/", defaults={"var": ""})
@app.route("/resources/<path:var>")
def getRes(var):
    intoPath = curPath / var
    if intoPath.exists():
        if intoPath.is_file():
            if intoPath.suffix == ".mp4":
                filename = intoPath.resolve()
                return send_file(filename, attachment_filename=filename, conditional=True)
            return send_file(intoPath.resolve())

    return "error"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
