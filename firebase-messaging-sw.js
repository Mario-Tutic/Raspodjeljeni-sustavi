// firebase-messaging-sw.js
importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging-compat.js");

// Initialize Firebase
const firebaseConfig = {
    apiKey: "AIzaSyAR6eZI97sTwAe502QHlRPdn7nwDuEWg8g",
    authDomain: "uber-copy-254c5.firebaseapp.com",
    projectId: "uber-copy-254c5",
    storageBucket: "uber-copy-254c5.firebasestorage.app",
    messagingSenderId: "275654718107",
    appId: "1:275654718107:web:1c440d11e94acefd7ecc3e",
    measurementId: "G-PD2K8PE1XT"
};

firebase.initializeApp(firebaseConfig);

// Retrieve an instance of Firebase Messaging
const messaging = firebase.messaging();

// Handle background messages
messaging.onBackgroundMessage((payload) => {
  console.log("Received background message: ", payload);

  // Customize notification here
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: payload.notification.icon,
  };

  // Show the notification
  self.registration.showNotification(notificationTitle, notificationOptions);
});