(function () {
  const registerPlugin = (editor) => {
    const portal_url = document.body.dataset.portalUrl;

    const openDialog = async () => {
      let icons = [];
      try {
        const response = await fetch(`${portal_url}/@@tinymce-icons-json`);
        const data = await response.json();
        icons = data.results || [];
      } catch (e) {
        console.error("Failed to fetch icons vocabulary", e);
      }

      const body = {
        type: "panel",
        items: [
          {
            type: "input",
            name: "search",
            label: "Search icons",
          },
          {
            type: "htmlpanel",
            html: '<div id="plone-icons-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(40px, 1fr)); gap: 10px; max-height: 300px; overflow-y: auto; margin-top: 10px;"></div>',
          },
        ],
      };

      const renderGrid = (filter = "") => {
        const grid = document.getElementById("plone-icons-grid");
        if (!grid) return;
        grid.innerHTML = "";

        if (icons.length === 0) {
          grid.innerHTML =
            '<div style="grid-column: 1 / -1; padding: 20px; text-align: center;">Loading icons or none found...</div>';
          return;
        }

        icons
          .filter((icon) =>
            icon.text.toLowerCase().includes(filter.toLowerCase()),
          )
          .forEach((icon) => {
            const btn = document.createElement("button");
            btn.type = "button";
            btn.title = icon.text;
            btn.style.cssText =
              "border: 1px solid #ddd; background: #fff; cursor: pointer; padding: 5px; display: flex; align-items: center; justify-content: center;";
            btn.innerHTML = `<img src="${portal_url}/@@iconresolver/${icon.id}" loading="lazy" style="width: 24px; height: 24px;" />`;
            btn.onclick = () => {
              editor.insertContent(
                `<img src="${portal_url}/@@iconresolver/${icon.id}" class="plone-icon-placeholder" data-val="${icon.id}" />`,
              );
              win.close();
            };
            grid.appendChild(btn);
          });
      };

      const win = editor.windowManager.open({
        title: "Insert Icon",
        body: body,
        buttons: [
          {
            type: "cancel",
            text: "Close",
            name: "cancel",
          },
        ],
        onTabChange: (dialogApi, details) => {
          renderGrid(dialogApi.getData().search);
        },
        onChange: (dialogApi, details) => {
          if (details.name === "search") {
            renderGrid(dialogApi.getData().search);
          }
        },
      });

      // Initial render - try several times to ensure the element is in DOM
      let attempts = 0;
      const tryRender = () => {
        const grid = document.getElementById("plone-icons-grid");
        if (grid) {
          renderGrid();
        } else if (attempts < 10) {
          attempts++;
          setTimeout(tryRender, 100);
        }
      };
      tryRender();

      // Also render when icons are finally loaded if they weren't yet
      const checkIcons = setInterval(() => {
        if (icons.length > 0) {
          renderGrid();
          clearInterval(checkIcons);
        }
        if (attempts >= 10) clearInterval(checkIcons);
      }, 200);
    };

    editor.ui.registry.addButton("ploneicons", {
      icon: "insert-character", // fallback icon
      tooltip: "Insert Icon",
      onAction: openDialog,
    });

    editor.ui.registry.addMenuItem("ploneicons", {
      icon: "insert-character",
      text: "Insert Icon",
      onAction: openDialog,
    });
  };

  const init = () => {
    if (typeof tinymce !== "undefined") {
      tinymce.PluginManager.add("ploneicons", registerPlugin);
    } else {
      setTimeout(init, 100);
    }
  };

  init();
})();
