import { useReducer, useEffect } from "react";
// import dbx from 'dropbox'
const UPLOAD_FILE_SIZE_LIMIT = 150 * 1024 * 1024;
// let storage =  new DropBoxStorage.DropBox({accessToken:process.env.REACT_APP_DROPBOX_SECRET})
const uploadFile = (e) => {
  e.preventDefault();
};
const DropBoxStorage = () => {
  return (
    <div>
      <p>
        This example shows how to use the <code>Dropbox.filesUpload()</code> [
        <a href="http://dropbox.github.io/dropbox-sdk-js/Dropbox.html#filesUpload">
          docs
        </a>
        ] method to upload a file.
      </p>
      <form onSubmit={uploadFile}>
        <input type="text" id="access-token" placeholder="Access token" />
        <input type="file" id="file-upload" />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};
export default DropBoxStorage;
