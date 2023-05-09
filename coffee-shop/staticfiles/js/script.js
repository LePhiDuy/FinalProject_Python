// some scripts

// jquery ready start
$(document).ready(function () {
  // jQuery code

  // Sự kiện click vào nút tăng số lượng
  $(document).on("click", ".qtybutton.inc", function () {
    var input = $(this).siblings(".cart-plus-minus-box");
    var currentValue = parseInt(input.val());
    input.val(currentValue + 1);
  });

  // Sự kiện click vào nút giảm số lượng
  $(document).on("click", ".qtybutton.dec", function () {
    var input = $(this).siblings(".cart-plus-minus-box");
    var currentValue = parseInt(input.val());
    if (currentValue > 1) {
      input.val(currentValue - 1);
    }
  });

  //////////////////////// Prevent closing from click inside dropdown
  $(document).on("click", ".dropdown-menu", function (e) {
    e.stopPropagation();
  });

  $(".js-check :radio").change(function () {
    var check_attr_name = $(this).attr("name");
    if ($(this).is(":checked")) {
      $("input[name=" + check_attr_name + "]")
        .closest(".js-check")
        .removeClass("active");
      $(this).closest(".js-check").addClass("active");
      // item.find('.radio').find('span').text('Add');
    } else {
      item.removeClass("active");
      // item.find('.radio').find('span').text('Unselect');
    }
  });

  $(".js-check :checkbox").change(function () {
    var check_attr_name = $(this).attr("name");
    if ($(this).is(":checked")) {
      $(this).closest(".js-check").addClass("active");
      // item.find('.radio').find('span').text('Add');
    } else {
      $(this).closest(".js-check").removeClass("active");
      // item.find('.radio').find('span').text('Unselect');
    }
  });

  //////////////////////// Bootstrap tooltip
  if ($('[data-toggle="tooltip"]').length > 0) {
    // check if element exists
    $('[data-toggle="tooltip"]').tooltip();
  } // end if

  var user = "{{request.user}}";

  function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getToken("csrftoken");

  function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for (var i = 0; i < cookieArr.length; i++) {
      var cookiePair = cookieArr[i].split("=");

      /* Removing whitespace at the beginning of the cookie name
            and compare it with the given string */
      if (name == cookiePair[0].trim()) {
        // Decode the cookie value and return
        return decodeURIComponent(cookiePair[1]);
      }
    }

    // Return null if not found
    return null;
  }
  var cart = JSON.parse(getCookie("cart"));

  if (cart == undefined) {
    cart = {};
    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  }

  var updateBtns = document.getElementsByClassName("update-cart");

  for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function (e) {
      e.preventDefault();
      var productID = this.dataset.product;
      var action = this.dataset.action;
      var input = $(this).siblings(".cart-plus-minus-box");
      // check if input exists
      var quantity ;
      if (input.length > 0) {
        quantity = parseInt(input.val());
      } else {
        quantity = 1;
      }

      if (user == "AnonymousUser") {
        addCookieItem(productID, action,quantity);
      } else {
        updateUserOrder(productID, action,quantity);
      }
    });
  }

  function addCookieItem(productID, action, quantity = 1) {
    console.log("Not logged in");
    if (action == "add") {
      if (cart[productID] == undefined) {
        cart[productID] = { quantity: 1 };
      } else {
        cart[productID]["quantity"] += quantity;
      }
    }

    if (action == "remove") {
      cart[productID]["quantity"] -= quantity;

      if (cart[productID]["quantity"] <= 0) {
        delete cart[productID];
      }
    }
    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();
  }

  function updateUserOrder(productID, action, quantity = 1) {
    console.log("User is logged in, sending data...");
    var url = "/update_item/";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
        productID: productID,
        action: action,
        quantity: quantity,
      }),
    })
      .then((response) => {
        return response.json();
      })

      .then((data) => {
        console.log("data:", data);
        location.reload();
      });
  }
});
// jquery end
