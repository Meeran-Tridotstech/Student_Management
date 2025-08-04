frappe.listview_settings['Jinja API'] = {
  // Fields available for formatting and filtering
  add_fields: ['status', 'priority', 'created_by'],

  // Hide default name column for cleaner UI
  hide_name_column: true,

  // Custom status indicators
  get_indicator(doc) {
    switch (doc.status) {
      case 'Approved':
        return ['✔️ Approved', 'green', 'status,=,Approved'];
      case 'Pending':
        return ['⏳ Pending', 'orange', 'status,=,Pending'];
      case 'Cancel':
        return ['❌ Cancel', 'red', 'status,=,Rejected'];
      default:
        return [doc.status || '🟦 Unknown', 'blue-grey', `status,=,${doc.status}`];
    }
  },

  // Custom column formatters with emoji and gradient text
  formatters: {
    status(val) {
      const gradients = {
        Approved: '#00c853, #64dd17',
        Pending: '#ffab00, #ff6f00',
        Cancel: '#d50000, #ff1744',
        Unknown: '#607d8b, #455a64'
      };
      const emojis = {
        Approved: '✔️',
        Pending: '⏳',
        Cancel: '❌',
        Unknown: '🔘'
      };
      const gradient = gradients[val] || gradients.Unknown;
      const emoji = emojis[val] || emojis.Unknown;
      return `<span style="background: linear-gradient(to right, ${gradient}); -webkit-background-clip: text; color: transparent; font-weight: bold;">${emoji} ${val}</span>`;
    },
    mail(val) {
      if (val) {
        return `<span style="color: #e53935; font-weight: bold;">🔥 ${val}</span>`;
      }
    }
  },

  // Contextual row button
  button: {
    show(doc) {
      return doc.status !== 'Closed';
    },
    get_label() {
      return '🔍 View';
    },
    get_description(doc) {
      return `View details of ${doc.name}`;
    },
    action(doc) {
      frappe.set_route('Form', 'Jinja API', doc.name);
    }
  },

};