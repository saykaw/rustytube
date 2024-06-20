// background.js

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "getBookmarks") {
      chrome.storage.sync.get("bookmarks", function (data) {
        sendResponse(data.bookmarks || []);
      });
      return true; // Indicates that the response will be sent asynchronously
    } else if (request.action === "addBookmark") {
      chrome.storage.sync.get("bookmarks", function (data) {
        var bookmarks = data.bookmarks || [];
        bookmarks.push(request.bookmark);
        chrome.storage.sync.set({ "bookmarks": bookmarks });
      });
    }
  });
  